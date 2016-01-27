import unittest
from tokenizer import Tokenizer

class TestBasicProcessing(unittest.TestCase):
    def test_tokenize(self):
        # with spaces and upper case:
        input_string1 =  "The rain in Spain"
        tokenizer1 = Tokenizer(input_string1)
        expected_list1 = ['the','rain','in','spain']
        self.assertEqual(expected_list1, tokenizer1.tokenize())
        # with other punctuation
        input_string2 = "I love you. I know. Do you? Yes, I do"
        tokenizer2 = Tokenizer(input_string2)
        expected_list2 = ["i", "love", "you", "i", "know", "do", "you", "yes", "i", "do"]
        self.assertEqual(expected_list2, tokenizer2.tokenize())
        # with apostrophes
        input_string3 = "You're a mean one, Mr. Grinch"
        tokenizer3 = Tokenizer(input_string3)
        expected_list3 = ["you're", "a", "mean", "one", "mr", "grinch"]
        self.assertEqual(expected_list3, tokenizer3.tokenize())

if __name__ == '__main__':
    unittest.main()
