from __future__ import annotations
import xmltodict
from typing import Optional
from .files import PathLike, save_file
from .interfaces import _IJsonLikeObj

class SimpleXml(_IJsonLikeObj):
    
    def __init__(self, data: dict, xml: Optional[str]=None, text_kw: str="#text", attrs_pref:str="@"):
        assert isinstance(data, dict)
        assert isinstance(xml, (str, type(None)))
        self.attrs_pref = attrs_pref
        self.text_kw = text_kw
        self.data = data
        self.xml = xml
    
    @staticmethod
    def upload_from_file(path: PathLike, text_kw="#text", attrs_pref="@") -> SimpleXml:
        with open(path, "r") as xml_file:
            data = xmltodict.parse(xml_file.read())
            return SimpleXml(data, text_kw=text_kw, attrs_pref=attrs_pref)
    
    @staticmethod
    def upload_from_str(xml: str, text_kw="#text", attrs_pref="@") -> SimpleXml:
        data = xmltodict.parse(xml, attr_prefix=attrs_pref, cdata_key=text_kw)
        return SimpleXml(data, xml, text_kw=text_kw, attrs_pref=attrs_pref)
    
    @staticmethod
    def upload_from_dict(data: dict, text_kw="#text", attrs_pref="@") -> SimpleXml:
        return SimpleXml(data, text_kw=text_kw, attrs_pref=attrs_pref)
    
    def upload_to_dict(self):
        "Will be removed soon"
        return self.get_dict()

    def get_xml(self):
        return xmltodict.unparse(self.data, pretty=True, attr_prefix=self.attrs_pref, cdata_key=self.text_kw)
    
    def get_dict(self):
        if self.data is not None:
            return self.data
        return xmltodict.parse(self.xml, attr_prefix=self.attrs_pref, cdata_key=self.text_kw)
        
    def save_file(self, path: PathLike, mode="+w"):
        save_file(path, self.get_xml(), mode)