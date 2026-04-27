from dataclasses import dataclass

from tempo_binary_tool_manager import manager


@dataclass(kw_only=True)
class FmodelToolInfo(manager.ToolInfo):
    tool_name: str = "FModel"
    repo_name: str = "FModel"
    repo_owner: str = "4sval"


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
