from pathlib import Path

from tempo_binary_tool_manager import manager


class StoveToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="stove",
            repo_name="stove",
            repo_owner="bananaturtlesandwich",
            cache=cache,
        )

    def __post_init__(self) -> None:
        if manager.is_windows():
            self.file_paths = [Path(f"{self.tool_name}.exe")]
        else:
            raise ValueError("unsupported os")


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return f"{self.tool_name}.exe"
        elif manager.is_linux():
            return f"{self.tool_name}-linux"
        else:
            raise ValueError("Unsupported OS")


    def get_executable_name(self) -> str:
        return self.get_file_to_download()
