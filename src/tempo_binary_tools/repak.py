from tempo_binary_tool_manager import manager


class RepakToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="repak",
            repo_name="repak",
            repo_owner="trumank",
            cache=cache,
        )


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'repak_cli-x86_64-pc-windows-msvc.zip'
        elif manager.is_linux():
            return 'repak_cli-x86_64-unknown-linux-gnu.tar.xz'
        else:
            raise ValueError('unsupported os')
