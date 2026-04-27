from dataclasses import dataclass

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class RepakToolInfo(manager.ToolInfo):
    tool_name: str = 'repak'
    repo_name: str = 'repak'
    repo_owner: str = 'trumank'


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'repak_cli-x86_64-pc-windows-msvc.zip'
        elif manager.is_linux():
            return 'repak_cli-x86_64-unknown-linux-gnu.tar.xz'
        else:
            raise ValueError('unsupported os')
