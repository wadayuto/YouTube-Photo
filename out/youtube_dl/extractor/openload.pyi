from ..compat import compat_kwargs as compat_kwargs, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, check_executable as check_executable, encodeArgument as encodeArgument, get_exe_version as get_exe_version, is_outdated_version as is_outdated_version, std_headers as std_headers
from typing import Any

def cookie_to_dict(cookie): ...
def cookie_jar_to_list(cookie_jar): ...

class PhantomJSwrapper:
    exe: Any
    extractor: Any
    options: Any
    def __init__(self, extractor, required_version: Any | None = ..., timeout: int = ...) -> None: ...
    def __del__(self) -> None: ...
    def get(self, url, html: Any | None = ..., video_id: Any | None = ..., note: Any | None = ..., note2: str = ..., headers=..., jscode: str = ...): ...