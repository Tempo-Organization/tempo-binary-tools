from pathlib import Path

from tempo_binary_tool_manager import manager


class TempoGitignoresToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="tempo_gitignores",
            repo_name="tempo-gitignores",
            repo_owner="Tempo-Organization",
            cache=cache,
        )


    def get_file_to_download(self) -> str:
        return 'tempo_gitignores.zip'


    def get_executable_name(self) -> str:
        # later have this be able to be none, and have the tool be used to non exe stuff
        return ''
