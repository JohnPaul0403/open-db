import unittest
from open_pydb import Data
class TestDataClass(unittest.TestCase):

    def test_init(self):
        data = Data(foo='bar', baz=42)
        self.assertEqual(data.foo, 'bar')
        self.assertEqual(data.baz, 42)

    def test_to_json(self):
        data = Data(foo='bar', baz=42)
        self.assertIsInstance(data.to_json(), Data)

    def test_ne(self):
        data1 = Data(foo='bar', baz=42)
        data2 = Data(foo='baz', baz=42)
        self.assertNotEqual(data1, data2)

    def test_eq(self):
        data1 = Data(foo='bar', baz=42)
        data2 = Data(foo='bar', baz=42)
        self.assertEqual(data1, data2)

    def test_hash(self):
        data1 = Data(foo='bar', baz=42)
        data2 = Data(foo='bar', baz=42)
        self.assertEqual(hash(data1), hash(data2))

    def test_repr(self):
        data = Data(foo='bar', baz=42)
        self.assertEqual(repr(data), "{'foo': 'bar', 'baz': 42}")

    def test_str(self):
        data = Data(foo='bar', baz=42)
        self.assertEqual(str(data), "{'foo': 'bar', 'baz': 42}")

    def test_iter(self):
        data = Data(foo='bar', baz=42)
        self.assertEqual(list(data), ['foo', 'baz'])

    def test_len(self):
        data = Data(foo='bar', baz=42)
        self.assertEqual(len(data), 2)

    def test_getitem(self):
        data = Data(foo='bar', baz=42)
        self.assertEqual(data['foo'], 'bar')

    def test_setitem(self):
        data = Data(foo='bar', baz=42)
        data['foo'] = 'baz'
        self.assertEqual(data.foo, 'baz')

if __name__ == '__main__':
    unittest.main()