import unittest

from .templates_utils import \
    unique_filename, path, \
    path_to_temp, path_to_samples, SimpleXml, remove
    
from .test_dicts import workers, animals, string_json_website, dict_json_website

class TestSimpleXml(unittest.TestCase):

    def test_convert(self):
        sx = SimpleXml.upload_from_file(path.join(path_to_samples, "test_xml_1.xml"))
        sx2 = SimpleXml.upload_from_dict(sx.get_dict())
        self.assertEqual(sx2.get_xml(), sx.get_xml())
        self.assertEqual(sx2.get_dict(), sx.get_dict())
        
    def test_convert_from_dict(self):
        sx_writer = SimpleXml.upload_from_file(path.join(path_to_samples, "test_xml_1.xml"))
        path_to_tempfile = path.join(path_to_temp, unique_filename() + ".xml") 
        sx_writer.save_file(path_to_tempfile)
        
        sx_reader = SimpleXml.upload_from_file(path_to_tempfile)
        sx_dict = SimpleXml.upload_from_dict(sx_reader.get_dict())
        self.assertEqual(sx_dict.get_xml(), sx_writer.get_xml())
        self.assertEqual(sx_dict.get_dict(), sx_writer.get_dict())
        remove(path_to_tempfile)