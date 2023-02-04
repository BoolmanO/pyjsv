import sys
from os.path import join
sys.path.append(join("pyjsv", "classes"))

from tests import TestSimpleJson, TestSimpleXml, TestXmlJsonConvert, TestSimpleToml, unittest


unittest.main()