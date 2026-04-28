from tempo_binary_tool_manager import manager



class UmodelToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="umodel",
            repo_name="UEViewer",
            repo_owner="Mythical-Github",
            cache=cache,
        )

    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'umodel_64.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'umodel_win32.zip'
        else:
            raise ValueError('unsupported os')
