from src/search_word import *
import unittest

class TestSearchWord(unnitest.TestCase):
  def test_wrong_key(self):
    wordtest   = "find"
    testapikey = "asdfer43tg23-sdfdf"
    expected   = "Error: Invalid API key. Not subscribed for this reference."
    self.assertEqual(webster_search(wordtest,testapikey), expected)
  
