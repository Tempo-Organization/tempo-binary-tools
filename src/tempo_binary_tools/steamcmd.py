from pathlib import Path
import requests

from kf1_mods_installer_gui import settings
from kf1_mods_installer_gui import manager as tool_manager

from tempo_binary_tool_manager import manager


def install_steamcmd(tool_info: manager.ToolInfo) -> None:
    tools_cache = tool_manager.tools_cache
    install_dir = tool_info.get_tool_directory()
    executable = install_dir / tool_info.get_executable_name()
    download_dir = tools_cache.get_download_dir()
    archive = download_dir / tool_info.get_file_to_download()

    if executable.is_file():
        tools_cache.logging_function("SteamCMD is already installed.")
        return

    install_dir.mkdir(parents=True, exist_ok=True)
    download_dir.mkdir(parents=True, exist_ok=True)

    tools_cache.logging_function(f"Downloading SteamCMD to {archive}...")

    response = requests.get(
        tool_info.get_download_url(),
        stream=True,
        timeout=15,
    )
    response.raise_for_status()

    with archive.open("wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    tools_cache.logging_function("  Download complete.")

    tools_cache.logging_function(f"Installing SteamCMD to {install_dir}...")
    manager.unpack_archive(archive, install_dir)

    if not executable.is_file():
        for path in install_dir.rglob(tool_info.get_executable_name()):
            if path.is_file():
                path.replace(executable)
                break

    archive.unlink(missing_ok=True)

    if not executable.is_file():
        raise RuntimeError(
            f"SteamCMD installation failed: {executable} was not found."
        )

    tools_cache.logging_function(f"  SteamCMD installed to: {install_dir}")


class SteamCmdToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="steam_cmd",
            repo_name=None,
            repo_owner=None,
            cache=cache,
            file_paths=[],
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'steamcmd.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'steamcmd.zip'
        else:
            raise ValueError('unsupported os')


    def get_download_url(self):
        return 'https://client-update.steamstatic.com/installer/steamcmd.zip'


    def get_tool_directory(self) -> Path:
        if not self.cache:
            raise RuntimeError('No tool cache somehow')
        return Path(settings.cache_dir / "tools" / 'steamcmd' / 'steamcmd' / 'Windows' / 'Static')


    def is_current_preferred_tool_version_installed(self):
        return Path(self.get_tool_directory() / self.get_executable_name()).is_file()


    def resolve_release_tag(self):
        return 'latest'


    def ensure_tool_installed(self):
        if not self.is_current_preferred_tool_version_installed():
            install_steamcmd(self)
