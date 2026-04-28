from pathlib import Path

from tempo_binary_tool_manager import manager


class SpaghettiToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="spaghetti",
            repo_name="spaghetti",
            repo_owner="bananaturtlesandwich",
            cache=cache,
            file_paths = [Path(self.get_file_to_download())],
        )


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
