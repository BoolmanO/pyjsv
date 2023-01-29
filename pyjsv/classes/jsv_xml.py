from __future__ import annotations
import xmltodict
from typing import Optional
from .files import PathLike, save_file

class SimpleXml:
    
    def __init__(self, data: dict, xml: Optional[str]=None, text_kw: str="#text", attrs_pref:str="@"):
        assert isinstance(data, dict)
        assert isinstance(xml, (str, type(None)))
        self.attrs_pref = attrs_pref
        self.text_kw = text_kw
        self.data = data
        self.xml = xml
    
    @staticmethod
    def upload_from_file(path: PathLike, text_kw="#text", attrs_pref="@", mode="r") -> SimpleXml:
        with open(path, mode) as xml_file:
            data = xmltodict.parse(xml_file.read())
            return SimpleXml(data, text_kw=text_kw, attrs_pref=attrs_pref)
    
    @staticmethod
    def upload_from_str(xml: str, text_kw="#text", attrs_pref="@") -> SimpleXml:
        data = xmltodict.parse(xml, attr_prefix=attrs_pref, cdata_key=text_kw)
        return SimpleXml(data, xml, text_kw=text_kw, attrs_pref=attrs_pref)
    
    @staticmethod
    def upload_from_dict(data: dict, text_kw="#text", attrs_pref="@") -> SimpleXml:
        return SimpleXml(data, text_kw=text_kw, attrs_pref=attrs_pref)

    def get_xml(self):
        return xmltodict.unparse(self.data, pretty=True, attr_prefix=self.attrs_pref, cdata_key=self.text_kw)
    
    def get_dict(self):
        if self.data is not None:
            return self.data
        return xmltodict.parse(self.xml, attr_prefix=self.attrs_pref, cdata_key=self.text_kw)
        
    def save_file(self, path: PathLike, mode="+w"):
        save_file(path, self.get_xml(), mode)


"Old Docs!"
"""
Explanation of dict to xml

The problem with xml is that it is completely different from dict
it can be converted to a dictionary or json, but an arbitrary dictionary cannot be easily converted to xml,
perhaps in the future I will add something that can connect these data structures.

Explanation of kw

The value of kw in variables is fate for the future,
xml has both text and key attributes,
kw - must be a unique string in which we write the text value that is in the element

for example:
    kw = 'field_text'
    <field2 name="asdfasd">some vlaue2</field2>
                           ^^^^^^^^^^^
                       will be written in kw
                       
    -> {'field2': [{'field_text': 'some vlaue2'}

I understand that the current interface for interacting with SimpleXml.data is not the best, 
in the future I will make an abstraction layer for more convenient interaction 
(the current method will still work)

"""