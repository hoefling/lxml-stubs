# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

import typing
from typing import Any, Dict, List, Mapping, MutableMapping, Tuple, Union, Optional, Sequence
from typing import Iterable, Iterator, SupportsBytes

from typing_extensions import Protocol


# We do *not* want `typing.AnyStr` because it is a `TypeVar`, which is an
# unnecessary constraint. It seems reasonable to constrain each
# List/Dict argument to use one type consistently, though, and it is
# necessary in order to keep these brief.
_AnyStr = Union[str, bytes]
_ListAnyStr = Union[List[str], List[bytes]]
_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
_Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]
_xpath = Union['XPath', _AnyStr]
_OptionalNamespace = Optional[Mapping[str, Any]]

class ElementChildIterator(Iterator['_Element']):
    def __iter__(self) -> 'ElementChildIterator': ...
    def __next__(self) -> '_Element': ...

class _Element(Iterable['_Element']):
    def addprevious(self, element: '_Element') -> None: ...
    def addnext(self, element: '_Element') -> None: ...
    def find(self, path: str, namespace: _OptionalNamespace = None)  -> '_Element': ...
    def findall(self, name: str, namespace: _OptionalNamespace = None) -> '_Element': ...
    def clear(self) -> None: ...
    def get(self, key: _AnyStr, default: Optional[_AnyStr] = ...) -> _AnyStr: ...
    def getparent(self) -> Optional[_Element]: ...
    def xpath(self, _path: _AnyStr, namespaces: Optional[_DictAnyStr] = ..., extensions: Any = ..., smart_strings: bool = ..., **_variables: Any) -> Any: ...
    # indeed returns a Union[bool, float, _AnyStr, List[Union[ElementBase, _AnyStr, Tuple[]]]]: ...
    # http://lxml.de/xpathxslt.html#xpath-return-values
    attrib = ...  # type: MutableMapping[str, str]
    text = ...  # type: _AnyStr
    tag = ...  # type: str
    def append(self, element: '_Element') -> '_Element': ...
    def __iter__(self) -> ElementChildIterator: ...
    def items(self) -> Sequence[Tuple[_AnyStr, _AnyStr]]: ...
    def iterfind(self, path: str, namespace: _OptionalNamespace = None)  -> Iterator['_Element']: ...

class ElementBase(_Element): ...

class _ElementTree:
    def getroot(self) -> _Element: ...
    def write(self,
              file: Union[_AnyStr, typing.IO],
              encoding: _AnyStr = ...,
              method: _AnyStr = ...,
              pretty_print: bool = ...,
              xml_declaration: Any = ...,
              with_tail: Any = ...,
              standalone: bool = ...,
              compression: int = ...,
              exclusive: bool = ...,
              with_comments: bool = ...,
              inclusive_ns_prefixes: _ListAnyStr = ...) -> None: ...
    def xpath(self,
              _path: _AnyStr,
              namespaces: Optional[_DictAnyStr] = ...,
              extensions: Any = ...,
              smart_strings: bool = ...,
              **_variables: Any) -> Any: ...
    def xslt(self,
             _xslt: XSLT,
             extensions: Optional[_Dict_Tuple2AnyStr_Any] = ...,
             access_control: Optional[XSLTAccessControl] = ...,
             **_variables) -> _ElementTree: ...

class QName:
    localname = ... # type: _AnyStr
    namespace = ... # type: _AnyStr
    text = ... # type: _AnyStr
    def __init__(self,
                 text_or_uri_element: Union[_AnyStr, _Element],
                 tag: Optional[_AnyStr] = ...) -> None: ...

class _XSLTResultTree(SupportsBytes):
    def __bytes__(self) -> bytes: ...

class _XSLTQuotedStringParam: ...


# https://lxml.de/parsing.html#the-target-parser-interface
class ParserTarget(Protocol):
    def comment(self, text: _AnyStr) -> None: ...
    def close(self) -> Any: ...
    def data(self, data: _AnyStr) -> None: ...
    def end(self, tag: _AnyStr) -> None: ...
    def start(self, tag: _AnyStr, attrib: _DictAnyStr) -> None: ...

class XMLParser:
    def __init__(self,
                 encoding: Optional[_AnyStr] = ...,
                 attribute_defaults: bool = ...,
                 dtd_validation: bool = ...,
                 load_dtd: bool = ...,
                 no_network: bool = ...,
                 ns_clean: bool = ...,
                 recover: bool = ...,
                 schema: Optional[XMLSchema] = ...,
                 huge_tree: bool = ...,
                 remove_blank_text: bool = ...,
                 resolve_entities: bool = ...,
                 remove_comments: bool = ...,
                 remove_pis: bool = ...,
                 strip_cdata: bool = ...,
                 collect_ids: bool = ...,
                 target: Optional[ParserTarget] = ...,
                 compact: bool = ...) -> None: ...

class XMLSchema:
    def __init__(self,
                 etree: Union[_Element, _ElementTree] = ...,
                 file: Union[_AnyStr, typing.IO] = ...) -> None: ...
    def assertValid(self, etree: Union[_Element, _ElementTree]) -> None: ...

class XSLTAccessControl: ...

class XSLT:
    def __init__(self,
                 xslt_input: Union[_Element, _ElementTree],
                 extensions: _Dict_Tuple2AnyStr_Any = ...,
                 regexp: bool = ...,
                 access_control: XSLTAccessControl = ...) -> None: ...
    def __call__(self,
                 _input: Union[_Element, _ElementTree],
                 profile_run: bool = ...,
                 **kwargs: Union[_AnyStr, _XSLTQuotedStringParam]) -> _XSLTResultTree: ...
    @staticmethod
    def strparam(s: _AnyStr) -> _XSLTQuotedStringParam: ...

def Element(_tag: _AnyStr,
            attrib: _DictAnyStr = ...,
            nsmap: _DictAnyStr = ...,
            **extra: _AnyStr) -> _Element: ...
def SubElement(_parent: _Element, _tag: _AnyStr,
               attrib: _DictAnyStr = ...,
               nsmap: _DictAnyStr = ...,
               **extra: _AnyStr) -> _Element: ...
def ElementTree(element: _Element = ...,
                file: Union[_AnyStr, typing.IO] = ...,
                parser: XMLParser = ...) -> _ElementTree: ...
def ProcessingInstruction(target: _AnyStr, text: _AnyStr = ...) -> _Element: ...
def parse(source: Union[_AnyStr, typing.IO],
          parser: XMLParser = ...,
          base_url: _AnyStr = ...) -> _ElementTree: ...
def fromstring(text: _AnyStr,
               parser: XMLParser = ...,
               *,
               base_url: _AnyStr = ...) -> _Element: ...
def tostring(element_or_tree: Union[_Element, _ElementTree],
             encoding: Union[str, type] = ...,
             method: str = ...,
             xml_declaration: bool = ...,
             pretty_print: bool = ...,
             with_tail: bool = ...,
             standalone: bool = ...,
             doctype: str = ...,
             exclusive: bool = ...,
             with_comments: bool = ...,
             inclusive_ns_prefixes: Any = ...) -> _AnyStr: ...

class _ErrorLog: ...

class Error(Exception): ...

class LxmlError(Error):
    def __init__(self, message: Any, error_log: _ErrorLog = ...) -> None: ...
    error_log = ...  # type: _ErrorLog

class DocumentInvalid(LxmlError): ...
class LxmlSyntaxError(LxmlError, SyntaxError): ...
class ParseError(LxmlSyntaxError): ...
class XMLSyntaxError(ParseError): ...

class _Validator: ...

class DTD(_Validator):
    def __init__(self,
                 file: Union[_AnyStr, typing.IO] = ...,
                 *,
                 external_id: Any = ...) -> None: ...

    def assertValid(self, etree: _Element) -> None: ...

class XPath:
    def __init__(self, path: _AnyStr, namespaces: Optional[_AnyStr], extensions: Optional[_AnyStr], regexp: Optional[bool], smart_strings: Optional[bool]) -> None: ...
