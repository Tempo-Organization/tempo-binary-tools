from dataclasses import dataclass

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class PatternsleuthToolInfo(manager.ToolInfo):
    tool_name: str = "patternsleuth"
    repo_name: str = "patternsleuth"
    repo_owner: str = "Tempo-Organization"


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'patternsleuth.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'patternsleuth-x86_64-pc-windows-msvc.zip'
        else:
            raise ValueError('unsupported os')
