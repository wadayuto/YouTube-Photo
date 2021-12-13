from ..compat import compat_cookiejar_Cookie as compat_cookiejar_Cookie, compat_cookies_SimpleCookie as compat_cookies_SimpleCookie, compat_etree_Element as compat_etree_Element, compat_etree_fromstring as compat_etree_fromstring, compat_getpass as compat_getpass, compat_http_client as compat_http_client, compat_integer_types as compat_integer_types, compat_os_name as compat_os_name, compat_str as compat_str, compat_urllib_error as compat_urllib_error, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode, compat_urllib_request as compat_urllib_request, compat_urlparse as compat_urlparse, compat_xml_parse_error as compat_xml_parse_error
from ..downloader.f4m import get_base_url as get_base_url, remove_encrypted_media as remove_encrypted_media
from ..utils import ExtractorError as ExtractorError, GeoRestrictedError as GeoRestrictedError, GeoUtils as GeoUtils, JSON_LD_RE as JSON_LD_RE, NO_DEFAULT as NO_DEFAULT, RegexNotFoundError as RegexNotFoundError, age_restricted as age_restricted, base_url as base_url, bug_reports_message as bug_reports_message, clean_html as clean_html, compiled_regex_type as compiled_regex_type, determine_ext as determine_ext, determine_protocol as determine_protocol, dict_get as dict_get, error_to_compat_str as error_to_compat_str, extract_attributes as extract_attributes, fix_xml_ampersands as fix_xml_ampersands, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_bitrate as parse_bitrate, parse_codecs as parse_codecs, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, parse_m3u8_attributes as parse_m3u8_attributes, parse_resolution as parse_resolution, sanitize_filename as sanitize_filename, sanitized_Request as sanitized_Request, str_or_none as str_or_none, str_to_int as str_to_int, strip_or_none as strip_or_none, unescapeHTML as unescapeHTML, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp, update_Request as update_Request, update_url_query as update_url_query, url_basename as url_basename, url_or_none as url_or_none, urljoin as urljoin, xpath_element as xpath_element, xpath_text as xpath_text, xpath_with_ns as xpath_with_ns
from typing import Any

class InfoExtractor:
    def __init__(self, downloader: Any | None = ...) -> None: ...
    @classmethod
    def suitable(cls, url): ...
    @classmethod
    def working(cls): ...
    def initialize(self) -> None: ...
    def extract(self, url): ...
    def set_downloader(self, downloader) -> None: ...
    @classmethod
    def ie_key(cls): ...
    @property
    def IE_NAME(self): ...
    def report_warning(self, msg, video_id: Any | None = ...) -> None: ...
    def to_screen(self, msg) -> None: ...
    def report_extraction(self, id_or_name) -> None: ...
    def report_download_webpage(self, video_id) -> None: ...
    def report_age_confirmation(self) -> None: ...
    def report_login(self) -> None: ...
    @staticmethod
    def raise_login_required(msg: str = ...) -> None: ...
    @staticmethod
    def raise_geo_restricted(msg: str = ..., countries: Any | None = ...) -> None: ...
    @staticmethod
    def url_result(url, ie: Any | None = ..., video_id: Any | None = ..., video_title: Any | None = ...): ...
    def playlist_from_matches(self, matches, playlist_id: Any | None = ..., playlist_title: Any | None = ..., getter: Any | None = ..., ie: Any | None = ...): ...
    @staticmethod
    def playlist_result(entries, playlist_id: Any | None = ..., playlist_title: Any | None = ..., playlist_description: Any | None = ...): ...
    def http_scheme(self): ...
    def get_testcases(self, include_onlymatching: bool = ...) -> None: ...
    def is_suitable(self, age_limit): ...
    def extract_subtitles(self, *args, **kwargs): ...
    def extract_automatic_captions(self, *args, **kwargs): ...
    def mark_watched(self, *args, **kwargs) -> None: ...
    def geo_verification_headers(self): ...

class SearchInfoExtractor(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
    @property
    def SEARCH_KEY(self): ...