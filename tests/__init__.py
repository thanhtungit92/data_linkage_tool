import unittest
import data_linkage_tool


class TestInitMethods(unittest.TestCase):
    def test(self):
        self.assertEqual(data_linkage_tool.dounittest(), 100)


if __name__ == '__main__':
    unittest.main()
