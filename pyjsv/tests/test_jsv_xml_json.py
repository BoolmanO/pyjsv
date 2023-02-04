import unittest

from .templates_utils import \
    unique_filename, path, \
    path_to_temp, SimpleJson, SimpleXml, remove
    
from .test_dicts import workers, animals, string_json_website, dict_json_website


class TestXmlJsonConvert(unittest.TestCase):
    def test_xml_json(self):
        some_values = \
            {"data": 
                {"developers": [
                    {"@country": "USA", "@rank": "Senior", "text": "Jony"},
                    {"@country": "Russia", "@rank": "Senior", "text": "Boris"}]
                }
            }
            
        sx = SimpleXml.upload_from_dict(some_values, text_kw="text")
        generated_xml = sx.get_xml()
        sx2 = SimpleXml.upload_from_str(generated_xml, text_kw="text") # generate dict by xml
        sj = SimpleJson.upload_from_dict(sx2.get_dict())
        self.assertEqual(sj.get_dict(), some_values)
        self.assertEqual(generated_xml, sx.get_xml())
        self.assertEqual(SimpleXml.upload_from_str(generated_xml, text_kw="text").get_dict(), sx.get_dict())
    