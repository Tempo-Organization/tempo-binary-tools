from dataclasses import dataclass

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class JmapToolInfo(manager.ToolInfo):
    tool_name: str = "jmap"
    repo_name: str = "jmap"
    repo_owner: str = "trumank"


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'jmap_dumper.exe'
        elif manager.is_linux():
            return 'jmap_dumper'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'jmap_dumper-x86_64-pc-windows-msvc.zip'
        elif manager.is_linux():
            return 'jmap_dumper-x86_64-unknown-linux-gnu.tar.xz'
        else:
            raise ValueError('unsupported os')
