from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str
from ..utils import js_to_json as js_to_json, strip_jsonp as strip_jsonp, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class WeiboIE(InfoExtractor): ...
class WeiboMobileIE(InfoExtractor): ...