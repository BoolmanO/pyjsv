import unittest

from .templates_utils import \
    unique_filename, path, \
    path_to_temp, SimpleJson, remove
    
from .test_dicts import workers, animals, string_json_website, dict_json_website

class TestSimpleJson(unittest.TestCase):

    def test_read_write_files(self):
        writer_sj = SimpleJson.upload_from_dict(animals)
        path_to_file = path.join(path_to_temp, unique_filename()) + ".json"
        writer_sj.save_file(path_to_file)
        reader_sj = SimpleJson.upload_from_file(path_to_file)
        #import time
        #time.sleep(5) if you want to see the file with your own eyes
        remove(path_to_file)
        self.assertEqual(writer_sj.data, reader_sj.data)
        
    def test_dicts_upload(self):
        sj = SimpleJson.upload_from_dict(workers)
        self.assertEqual(sj.data, workers)
        
    def test_string_upload(self):
        string_json = string_json_website
        sj = SimpleJson.upload_from_str(string_json)
        self.assertEqual(sj.data, dict_json_website)