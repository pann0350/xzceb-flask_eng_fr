import unittest
from translator import french_to_english, english_to_french


class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_englishToFrench2(self):
        self.assertEqual(english_to_french("French method"), "Méthode française")

    def test_englishToFrench3(self):
        self.assertNotEqual(english_to_french(0), 0)

    def test_englishToFrench4(self):
        self.assertNotEqual(english_to_french("None"), "")


    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_frenchToEnglish2(self):
        self.assertEqual(
            french_to_english("Je teste cette méthode"), "I'm testing this method"
        )

    def test_frenchToEnglish3(self):
        self.assertNotEqual(french_to_english(0), 0)

    def test_frenchToEnglish4(self):
        self.assertNotEqual(french_to_english("None"), "")


unittest.main()
