from __future__ import annotations
import xmltodict
from typing import Optional
from .files import PathLike, save_file
from .interfaces import _IJsonLikeObj


class SimpleXml(_IJsonLikeObj):
    def __init__(self, data: dict[str, list], xml: Optional[str]=None, text_kw: str="#text", attrs_pref:str="@"):
        self.attrs_pref = attrs_pref
        self.text_kw = text_kw
        self.data = data
        self.xml = xml
    
    @staticmethod
    def upload_from_dict(data: dict[str, list], text_kw="#text", attrs_pref="@") -> SimpleXml:
        """The dictionary to be loaded must conform to the following structure: [str:list], where str is the root tag \n
        If you are unsure and want to see examples, you can take them from tests or documentation, at the bottom of pyjsv\classes\jsv_xml.py \n 
        there is also an example and answers to questions"""
        return SimpleXml(data, text_kw=text_kw, attrs_pref=attrs_pref)

    @staticmethod
    def upload_from_str(xml: str, text_kw="#text", attrs_pref="@") -> SimpleXml:
        data = xmltodict.parse(xml, attr_prefix=attrs_pref, cdata_key=text_kw)
        return SimpleXml(data, xml, text_kw=text_kw, attrs_pref=attrs_pref)

    @staticmethod
    def upload_from_file(path: PathLike, text_kw="#text", attrs_pref="@") -> SimpleXml:
        with open(path, "r") as xml_file:
            data = xmltodict.parse(xml_file.read())
            return SimpleXml(data, text_kw=text_kw, attrs_pref=attrs_pref)

    def get_xml(self):
        return xmltodict.unparse(self.data, pretty=True, attr_prefix=self.attrs_pref, cdata_key=self.text_kw)
    
    def get_dict(self):
        if self.data is not None:
            return self.data
        return xmltodict.parse(self.xml, attr_prefix=self.attrs_pref, cdata_key=self.text_kw)
        
    def save_file(self, path: PathLike, mode="+w"):
        save_file(path, self.get_xml(), mode)
        
        
"""
SimpleXml specification:
    Saving files in .xml format,
    loading data from dict (you can load data in dict format (i.e. json) and save as .xml)
    
FAQ:

Q: What is text_kw?
A: text_kw defines the name of a dictionary key that stores data with the text of a specific tag

Q: What is attrs_pref?
A: attrs_pref is an attribute prefix, 
   it is necessary in order to be able to distinguish between the attributes of the tag itself and its children
   
Q: How can i load a dict into xml format without errors?
A: Suppose you have the following dict:
{"data": 
    {"developers": [
        {"country": "USA", "rank": "Senior", "name": "Jony"},
        {"country": "Russia", "rank": "Senior", "name": "Boris"}
        ]
    }
}
   Are you expecting to receive:

    <?xml version="1.0" encoding="utf-8"?>
    <data>
        <developers country="USA" rank="Senior">Jony</developers>     
        <developers country="Russia" rank="Senior">Boris</developers> 
    </data>
    
    To serialize correctly and place for example the name field in the text value of the tag
    You must specify text_kw
    and add a prefix to the expected attributes in the dictionary, by default @
    
    updated dict:
    {"data": 
        {"developers": [
            {"@country": "USA", "@rank": "Senior", "name": "Jony"},
            {"@country": "Russia", "@rank": "Senior", "name": "Boris"}]
        }
    }
    code:
    sx = SimpleXml.upload_from_dict(some_values, text_kw="name")
"""