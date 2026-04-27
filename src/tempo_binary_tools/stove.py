from dataclasses import dataclass, field
from pathlib import Path

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class StoveToolInfo(manager.ToolInfo):
    tool_name: str = "stove"
    repo_name: str = "stove"
    repo_owner: str = "bananaturtlesandwich"
    file_paths: list[Path] = field(default_factory=list)

    def __post_init__(self):
        self.file_paths = [Path(self.get_file_to_download())]

    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return f"{self.tool_name}.exe"
        elif manager.is_linux():
            return f"{self.tool_name}-linux"
        else:
            raise ValueError("Unsupported OS")

    def get_executable_name(self) -> str:
        return self.get_file_to_download()
