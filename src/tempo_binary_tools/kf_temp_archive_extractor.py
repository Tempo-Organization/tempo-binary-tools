from pathlib import Path

from tempo_binary_tool_manager import manager


class KfTempArchiveExtractorToolInfo(manager.ToolInfo):
    def __init__(self, cache: manager.ToolsCache) -> None:
        super().__init__(
            tool_name="kf_temp_archive_extractor",
            repo_name="KFTempArchiveExtractor",
            repo_owner="KillingFloorSeriesModding",
            cache=cache,
            file_paths=[Path('KFTempArchiveExtractor.exe')],
        )


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'KFTempArchiveExtractor.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'KFTempArchiveExtractor.exe'
        else:
            raise ValueError('unsupported os')
