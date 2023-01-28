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
        
    def test_upload_from_str(self):
        string_xml = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
        <field2 name="asdfasd">some vlaue2</field2>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''
        sx = SimpleXml.upload_from_str(string_xml, kw="text")
        country = sx.data['data'][0]["country"]
        self.assertEqual(country[3]["gdppc"][0]['text'], '141100') # It will look better in the future
        self.assertEqual(country[0]["name"], 'Liechtenstein')