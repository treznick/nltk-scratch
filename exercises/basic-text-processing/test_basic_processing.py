import unittest
from tokenizer import Tokenizer

class TestBasicProcessing(unittest.TestCase):

    def test_tokenize_with_spaces(self):
        input_string =  "the rain in spain"
        tokenizer = Tokenizer(input_string)
        expected_list = ['the','rain','in','spain']
        self.assertEqual(expected_list, tokenizer.tokenize())

    def test_tokenize_with_spaces_and_downcasing(self):
        input_string =  "The rain in Spain"
        tokenizer = Tokenizer(input_string)
        expected_list = ['the','rain','in','spain']
        self.assertEqual(expected_list, tokenizer.tokenize())

    def test_tokenize_with_other_punctuation(self):
        input_string = "I love you. I know. Do you? Yes, I do"
        tokenizer = Tokenizer(input_string)
        expected_list = ["i", "love", "you", "i", "know", "do", "you", "yes", "i", "do"]
        self.assertEqual(expected_list, tokenizer.tokenize())

    def test_tokenize_with_apostrophes(self):
        input_string = "You're a mean one, Mr. Grinch"
        tokenizer = Tokenizer(input_string)
        expected_list = ["you're", "a", "mean", "one", "mr", "grinch"]
        self.assertEqual(expected_list, tokenizer.tokenize())

if __name__ == '__main__':
    unittest.main()
