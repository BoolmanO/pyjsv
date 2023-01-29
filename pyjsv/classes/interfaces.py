from abc import ABC, abstractmethod, abstractstaticmethod
from .files import PathLike

class _IJsonLikeObj(ABC):
    # TODO: add comments, annotations
    
    def __init__(self, dict_obj: dict):
        assert isinstance(dict_obj, dict)
        self.data = dict_obj
        
    def __repr__(self):
        return f"<{self.__class__}: {self.data}>"
    
    @abstractstaticmethod
    def upload_from_dict(to_json: dict) -> "_IJsonLikeObj": pass
    
    @abstractstaticmethod
    def upload_from_str(to_json: str) -> "_IJsonLikeObj": pass
    
    @abstractstaticmethod
    def upload_from_file(to_json: PathLike) -> "_IJsonLikeObj": pass
    
    
    @abstractmethod
    def save_file(self, path: PathLike): pass
    
    @abstractmethod
    def get_dict(self) -> dict: pass
    