import unittest
from os import name


class TestCommentInputField(unittest.TestCase):
    def setUp(self):
        self.input_field = ""

    def test_na_alfavit(self):
        input_text = "Hello World"
        self.input_field = input_text
        self.assertEqual(self.input_field, input_text)

    def test_na_nomera(self):
        input_text = "123456"
        self.input_field = input_text
        self.assertEqual(self.input_field, input_text)

    def test_speskal_simvols(self):
        input_text = "!@#$%^&*()"
        self.input_field = input_text
        self.assertEqual(self.input_field, input_text)

    def test_smes(self):
        input_text = "Hello123!@#"
        self.input_field = input_text
        self.assertEqual(self.input_field, input_text)

    def test_prostranstvo(self):
        input_text = "   Hello   World   "
        self.input_field = input_text
        self.assertEqual(self.input_field.strip(), "Hello   World")

    def test_empty_input(self):
        input_text = ""
        self.input_field = input_text
        self.assertEqual(self.input_field, input_text)

    def test_long(self):
        input_text = "a" * 1000
        self.input_field = input_text
        self.assertEqual(self.input_field, input_text)




if name == "__main__":
    unittest.main()