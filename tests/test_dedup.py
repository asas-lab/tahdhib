import unittest
from dataset_cleaner.deduplication import exact_deduplication

class TestExactDeduplication(unittest.TestCase):

    def test_remove_harkat(self):
        result = exact_deduplication('samples.json.gz')
        self.assertEqual(result, "Done")


if __name__ == '__main__':
    unittest.main()
