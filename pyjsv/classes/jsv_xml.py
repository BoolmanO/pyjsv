import xml.etree.ElementTree as ET
from typing import Optional
from .files import PathLike, save_file

class SimpleXml:
    data: dict
    
    def __init__(self, data, tree: Optional[ET.ElementTree] = None, kw: str ="__xml__text__in__field"):
        assert isinstance(data, dict)
        assert isinstance(tree, (ET.ElementTree, type(None)))
        assert isinstance(kw, str)
        self.data = data
        self.__tree = tree
        self.kw = kw
    
    @staticmethod
    def _upload_from_elem(elem: ET.Element, kw: str="__xml__text__in__field") -> "SimpleXml":
        tree = ET.ElementTree(elem)
        return SimpleXml._upload_from_tree(tree, kw)
    
    @staticmethod
    def _upload_from_tree(tree: ET.ElementTree, kw: str="__xml__text__in__field") -> "SimpleXml":
        assert isinstance(tree, ET.ElementTree)
        root = tree.getroot()
        temp = []
        
        for child in root:
            chtmp = []
            
            if child.attrib is not None:
                chtmp.append(child.attrib)
            
            for i in root.findall(child.tag+"/*"):
                chtmp.append({i.tag: [{kw: i.text}, i.attrib]})
                
            temp.append({child.tag: chtmp})
            
        return SimpleXml({root.tag: temp}, tree, kw)
    
    @staticmethod
    def upload_from_dict(to_xml: dict, kw: str="__xml__text__in__field") -> "SimpleXml":
        raise NotImplementedError("See sources for explanation of current position with xml and dict")
        #return SimpleXml(to_xml, kw=kw) # No tree
    
    @staticmethod
    def upload_from_str(to_xml: str, kw: str="__xml__text__in__field") -> "SimpleXml":
        elem = ET.fromstring(to_xml)
        return SimpleXml._upload_from_elem(elem, kw)
    
    @staticmethod
    def upload_from_file(to_xml: PathLike, kw: str="__xml__text__in__field") -> "SimpleXml":
        tree = ET.parse(to_xml)
        return SimpleXml._upload_from_tree(tree, kw)
    
    def get_xml(self, encoding="utf-8") -> str:
        if self.__tree:
            return ET.tostring(self.__tree.getroot(), encoding=encoding, method="xml").decode(encoding) 

        raise NotImplementedError("See sources for explanation of current position with xml and dict")
        
    def upload_to_dict(self) -> dict:
        return self.data
    
    def save_file(self, path: PathLike):
        save_file(path, self.get_xml())
    

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