from pathlib import Path

from tempo_binary_tool_manager import manager


class UassetGuiToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="uasset_gui",
            repo_name="UAssetGUI",
            repo_owner="atenfyr",
            cache=cache,
            file_paths=[Path('UAssetGUI.exe')],
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'UAssetGUI.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'UAssetGUI.exe'
        else:
            raise ValueError('unsupported os')
