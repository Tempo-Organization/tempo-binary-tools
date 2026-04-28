from tempo_binary_tool_manager import manager


class InjectorToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="injector",
            repo_name="injector",
            repo_owner="nefarius",
            cache=cache,
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'x64/Injector.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'Injector_x86_amd64_arm64.zip'
        else:
            raise ValueError('unsupported os')
