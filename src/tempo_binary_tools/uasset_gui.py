from dataclasses import dataclass, field
from pathlib import Path

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class UassetGuiToolInfo(manager.ToolInfo):
    tool_name: str = "uasset_gui"
    repo_name: str = "UAssetGUI"
    repo_owner: str = "atenfyr"
    file_paths: list[Path] = field(default_factory=lambda: [Path('UAssetGUI.exe')])


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
