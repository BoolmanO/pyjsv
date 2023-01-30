from __future__ import annotations
from abc import ABC, abstractmethod, abstractstaticmethod
from .files import PathLike

class _IJsonLikeObj(ABC):  
    def __init__(self, dict_obj: dict):
        self.data = dict_obj
        
    def __repr__(self):
        return f"<{self.__class__}>"
    
    @abstractstaticmethod
    def upload_from_dict(to_json: dict) -> _IJsonLikeObj: pass
    
    @abstractstaticmethod
    def upload_from_str(to_json: str) -> _IJsonLikeObj: pass
    
    @abstractstaticmethod
    def upload_from_file(to_json: PathLike) -> _IJsonLikeObj: pass
    
    @abstractmethod
    def save_file(self, path: PathLike): pass
    
    @abstractmethod
    def get_dict(self) -> dict: pass
    
"""
You can rely on this interface, all classes inherit from this abstract class, 
but it is worth remembering that it is possible to add class-specific key words
"""