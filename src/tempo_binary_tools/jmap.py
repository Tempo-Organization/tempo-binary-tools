from tempo_binary_tool_manager import manager


class JmapToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="jmap",
            repo_name="jmap",
            repo_owner="trumank",
            cache=cache,
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'jmap_dumper.exe'
        elif manager.is_linux():
            return 'jmap_dumper'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'jmap_dumper-x86_64-pc-windows-msvc.zip'
        elif manager.is_linux():
            return 'jmap_dumper-x86_64-unknown-linux-gnu.tar.xz'
        else:
            raise ValueError('unsupported os')
