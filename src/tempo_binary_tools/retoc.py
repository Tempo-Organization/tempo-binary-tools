from packaging.version import Version
from dataclasses import dataclass

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class RetocToolInfo(manager.ToolInfo):
    tool_name: str = "retoc"
    repo_name: str = "retoc"
    repo_owner: str = "trumank"


    def get_download_url(self) -> str:
        release_tag = self.get_current_preferred_release_tag()

        version = Version(release_tag.lstrip("v"))

        if version >= Version("0.1.5"):
            base_url_prefix = (
                f"https://github.com/{self.repo_owner}/{self.repo_name}/releases/download/"
                f"{release_tag}/retoc_cli-x86_64-"
            )
        else:
            base_url_prefix = (
                f"https://github.com/{self.repo_owner}/{self.repo_name}/releases/download/"
                f"{release_tag}/retoc-x86_64-"
            )

        if manager.is_windows():
            return f"{base_url_prefix}pc-windows-msvc.zip"
        elif manager.is_linux():
            return f"{base_url_prefix}unknown-linux-gnu.tar.xz"
        else:
            raise ValueError("unsupported os")


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return "retoc_cli-x86_64-pc-windows-msvc.zip"
        elif manager.is_linux():
            return "retoc-x86_64-unknown-linux-gnu.tar.xz"
        else:
            raise ValueError("unsupported os")
