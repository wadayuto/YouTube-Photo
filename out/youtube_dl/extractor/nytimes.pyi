from ..utils import determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, remove_start as remove_start
from .common import InfoExtractor as InfoExtractor

class NYTimesBaseIE(InfoExtractor): ...
class NYTimesIE(NYTimesBaseIE): ...
class NYTimesArticleIE(NYTimesBaseIE): ...
class NYTimesCookingIE(NYTimesBaseIE): ...