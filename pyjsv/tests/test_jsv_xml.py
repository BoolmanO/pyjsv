import unittest

from .templates_utils import \
    unique_filename, path, \
    path_to_temp, path_to_samples, SimpleXml, remove
    
from .test_dicts import workers, animals, string_json_website, dict_json_website

class TestSimpleXml(unittest.TestCase):

    def test_read_files(self):
        sx = SimpleXml.upload_from_file(path.join(path_to_samples, "test_xml_1.xml"), kw="text")
        country = sx.data['data'][0]["country"]
        self.assertEqual(country[3]["gdppc"][0]['text'], '141100') # It will look better in the future
        self.assertEqual(country[0]["name"], 'Liechtenstein')
        
    def test_write_files(self):
        sx_writer = SimpleXml.upload_from_file(path.join(path_to_samples, "test_xml_1.xml"), kw="text")
        path_to_temp_xml = path.join(path_to_temp, unique_filename())+".xml"
        sx_writer.save_file(path_to_temp_xml)
        sx_reader = SimpleXml.upload_from_file(path_to_temp_xml, kw="text")
        self.assertEqual(sx_writer.data, sx_reader.data)
        remove(path_to_temp_xml)