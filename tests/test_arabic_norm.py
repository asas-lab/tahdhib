import unittest
from dataset_cleaner.normalize_arabic import normalize

class TestArabicNormalization(unittest.TestCase):

    def test_remove_harkat(self):
        text = "العَرَبِيَّةُ"
        normalized = normalize(text, remove_harkat=True)
        self.assertEqual(normalized, "العربية")

    def test_unified_alf(self):
        text = "أإآا"
        normalized = normalize(text, unified_alf=True)
        self.assertEqual(normalized, "اااا")

    def test_unified_yaa(self):
        text = "ى"
        normalized = normalize(text, unified_yaa=True)
        self.assertEqual(normalized, "ي")

    def test_remove_tatweel(self):
        text = "بـسـم الله الــرحمن الرحيـــــــمــ"
        normalized = normalize(text, remove_tatweel=True)
        self.assertEqual(normalized, "بسم الله الرحمن الرحيم")

    def test_remove_extrawhitespaces(self):
        text = "ذهب  أحمد إلى المسجد  "
        normalized = normalize(text, remove_extrawhitespace=True)
        self.assertEqual(normalized, "ذهب أحمد إلى المسجد")


if __name__ == '__main__':
    unittest.main()
