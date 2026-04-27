from dataclasses import dataclass, field
from pathlib import Path

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class SpaghettiToolInfo(manager.ToolInfo):
    tool_name: str = "spaghetti"
    repo_name: str = "spaghetti"
    repo_owner: str = "bananaturtlesandwich"
    file_paths: list[Path] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.file_paths = [Path(self.get_file_to_download())]


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'spaghetti.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'spaghetti.exe'
        else:
            raise ValueError('unsupported os')
