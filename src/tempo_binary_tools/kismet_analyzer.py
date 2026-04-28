from tempo_binary_tool_manager import manager
from tempo_binary_tools import git


class KismetAnalyzerToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="kismet_analyzer",
            repo_name="kismet-analyzer",
            repo_owner="trumank",
            cache=cache,
        )


    def get_file_to_download(self) -> str:
        # FIX: never allow invalid hash strings to propagate
        commit_short_hash = git.get_commit_short_hash_from_tag(
            repo_name="trumank/kismet-analyzer",
            is_online=True,
            tag_name="latest",
        )

        if not commit_short_hash or len(commit_short_hash) != 7:
            raise RuntimeError(
                f"Invalid commit hash returned from GitHub API: {commit_short_hash}"
            )

        if manager.is_windows():
            return f"{self.repo_name}-{commit_short_hash}-win-x64.zip"
        elif manager.is_linux():
            return f"{self.repo_name}-{commit_short_hash}-linux-x64.zip"
        else:
            raise ValueError("Unsupported OS")


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return f"{self.repo_name}.exe"
        elif manager.is_linux():
            return f"{self.repo_name}"
        else:
            raise ValueError("Unsupported OS")
