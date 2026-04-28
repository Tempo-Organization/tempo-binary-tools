from tempo_binary_tool_manager import manager


class UEVRMcpToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="ue_vr_mcp",
            repo_name="uevr-mcp",
            repo_owner="elliotttate",
            cache=cache,
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return ''
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return ''
        else:
            raise ValueError('unsupported os')
