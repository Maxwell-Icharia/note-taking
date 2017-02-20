import unittest, main
from main.note import list_input

class NoteTests(unittest.TestCase):

    def test_is_list(self):
        self.assertNotEqual(list_input(3), 'm')

if __name__ == '__main__':
    unittest.main()
