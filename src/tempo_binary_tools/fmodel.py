from tempo_binary_tool_manager import manager


class FmodelToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="fmodel",
            repo_name="FModel",
            repo_owner="4sval",
            cache=cache,
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'FModel.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'Fmodel.zip'
        else:
            raise ValueError('unsupported os')
