from tempo_binary_tool_manager import manager


class UEVRToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="ue_vr",
            repo_name="UEVR",
            repo_owner="praydog",
            cache=cache,
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'UEVRInjector.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'UEVR.zip'
        else:
            raise ValueError('unsupported os')
