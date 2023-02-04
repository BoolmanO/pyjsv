import unittest
from .templates_utils import \
    unique_filename, path, \
    path_to_temp, path_to_samples, SimpleToml, remove

class TestSimpleToml(unittest.TestCase):
    def test_convert(self):
        st = SimpleToml.upload_from_file(path.join(path_to_samples, "test_toml_1.toml"))
        toml_dict = \
        {
        'table': {'foo': 'bar', 'amogus': 'VERY SUS!'}, 
        'log': {'dev_branch': True, 'any_int': 5}, 
        'toml': {'authors': ['name1', 'name2', 'name3']}, 
        'any_table': {'any': 'data'}, 
        'servers': {
                    'alpha': {'ip': '127.0.0.1', 'port': '8000'}, 
                    'beta': {'ip': '127.0.0.1', 'port': '8001'}
                    }
        }
        toml_str = \
'''[table]
foo = "bar"
amogus = "VERY SUS!"

[log]
dev_branch = true
any_int = 5

[toml]
authors = ["name1", "name2", "name3"]

[any_table]
any = "data"

[servers]

    # comment
    [servers.alpha]
    ip = "127.0.0.1"
    port = "8000"

    [servers.beta]
    ip = "127.0.0.1"
    port = "8001"'''

        self.assertEqual(st.get_dict(), toml_dict)
        st_str = SimpleToml.upload_from_str(toml_str)
        self.assertEqual(st.get_dict(), st_str.get_dict())
        self.assertEqual(st.get_toml(), st_str.get_toml())

    def test_read_write_files(self):
        st = SimpleToml.upload_from_file(path.join(path_to_samples, "test_toml_1.toml"))
        path_to_tempfile = path.join(path_to_temp, unique_filename() + ".toml")
        st.save_file(path_to_tempfile)
        st_reader = SimpleToml.upload_from_file(path_to_tempfile)
        self.assertEqual(st.get_dict(), st_reader.get_dict())
        self.assertEqual(st.get_toml(), st_reader.get_toml())
        remove(path_to_tempfile) 