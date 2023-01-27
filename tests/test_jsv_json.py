#import tempfile do this in future
import unittest
from os.path import join
from pyjsv import SimpleJson
from .templates_utils import unique_filename
from .test_dicts import workers, animals

class TestSimpleJsonDict(unittest.TestCase):

    def test_workers(self):
        sj = SimpleJson.load_from_dict(workers)
        path_to_file = f"{join("tempfile",unique_filename())}.json"
        #self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()