from __future__ import annotations
import xmltodict
from typing import Optional
from .files import PathLike, save_file, OpenTextMode
from .interfaces import _IJsonLikeObj


class SimpleXml(_IJsonLikeObj):
    def __init__(self, data: dict[str, list], xml: Optional[str]=None, 
                text_key: str="#text", attr_prefix:str="@"):
        """
        Initialize a SimpleXml instance.

        :param data: XML data as a dictionary
        :param xml: XML data as a string
        :param text_key: key used to store the text of a specific tag
        :param attr_prefix: prefix used to distinguish between tag attributes and its children
        """
        self.attr_prefix = attr_prefix
        self.text_key = text_key
        self.data = data
        self.xml = xml
    
    @staticmethod
    def from_dict(to_xml: dict[str, list], text_key: str="#text", attr_prefix: str="@") -> SimpleXml:
        """The dictionary to be loaded must conform to the following structure: {str:list}, where str is the root tag \n
        If you are unsure and want to see examples, you can take them from tests or documentation, at the bottom of pyjsv\classes\jsv_xml.py \n 
        there is also an example and answers to questions"""
        return SimpleXml(to_xml, text_key=text_key, attr_prefix=attr_prefix)

    @staticmethod
    def from_string(xml: str, text_key: str="#text", attr_prefix: str="@") -> SimpleXml:
        data = xmltodict.parse(xml, attr_prefix=attr_prefix, cdata_key=text_key)
        return SimpleXml(data, xml, text_key=text_key, attr_prefix=attr_prefix)

    @staticmethod
    def from_file(path: PathLike, text_key: str="#text", attr_prefix: str="@", mode: OpenTextMode = "r") -> SimpleXml:
        with open(path, mode) as xml_file:
            data = xmltodict.parse(xml_file.read())
            return SimpleXml(data, text_key=text_key, attr_prefix=attr_prefix)

    def get_xml(self) -> str:
        "Returns the `xml` string representation of the data stored in the class."
        return xmltodict.unparse(self.data, pretty=True, attr_prefix=self.attr_prefix, cdata_key=self.text_key)
    
    def get_dict(self) -> dict[str, list]:
        "Returns the dictionary representation of the data stored in the class."
        if self.data is not None:
            return self.data
        return xmltodict.parse(self.xml, attr_prefix=self.attr_prefix, cdata_key=self.text_key)
        
    def save_file(self, path: PathLike, mode: OpenTextMode="+w") -> None:
        "Saves the data (in `xml` format) stored in the class to a file."
        save_file(path, self.get_xml(), mode)
        
        
"""
SimpleXml specification:
    Saving files in .xml format,
    loading data from dict (you can load data in dict format (i.e. json) and save as .xml)
    
FAQ:

Q: What is text_key?
A: text_key defines the name of a dictionary key that stores data with the text of a specific tag

Q: What is attr_prefix?
A: attr_prefix is an attribute prefix, 
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
    You must specify text_key
    and add a prefix to the expected attributes in the dictionary, by default @
    
    updated dict:
    {"data": 
        {"developers": [
            {"@country": "USA", "@rank": "Senior", "name": "Jony"},
            {"@country": "Russia", "@rank": "Senior", "name": "Boris"}]
        }
    }
    code:
    sx = SimpleXml.from_dict(some_values, text_key="name")
"""