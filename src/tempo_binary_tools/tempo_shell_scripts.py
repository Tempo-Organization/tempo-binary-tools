from pathlib import Path

from tempo_binary_tool_manager import manager


class TempoShellScriptsToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="tempo_shell_scripts",
            repo_name="tempo-shell-scripts",
            repo_owner="Tempo-Organization",
            cache=cache,
        )


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'batch.zip'
        elif manager.is_linux():
            return 'sh.zip'
        else:
            raise ValueError("Unsupported OS")


    def get_executable_name(self) -> str:
        # later have this be able to be none, and have the tool be used to non exe stuff
        return ''
