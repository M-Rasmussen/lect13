'''
    split_test.py
    
    This file tests string.split(). In the real world, there's no need to test
    Python's library functions, but we're just doing this as an intro to unit
    tests.
'''

import unittest

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
KEY_FIRST_WORD = "first_word"
KEY_SECOND_WORD = "second_word"

class SplitTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            #SplitTestOject()
            {
                KEY_INPUT: "Childish Gambino",
                KEY_EXPECTED: {
                    KEY_LENGTH: 2,
                    KEY_FIRST_WORD: "Childish",
                    KEY_SECOND_WORD: "Gambino",
                }
            },
            {
                KEY_INPUT: "Bone Thugs N' Harmony",
                KEY_EXPECTED: {
                    KEY_LENGTH: 4,
                    KEY_FIRST_WORD: "Bone",
                    KEY_SECOND_WORD: "Thugs",
                }
            },
            {
                KEY_INPUT: "Joe Strummer",
                KEY_EXPECTED: {
                    KEY_LENGTH: 2,
                    KEY_FIRST_WORD: "Joe",
                    KEY_SECOND_WORD: "Strummer",
                }
            }

        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT: "Nicki Minaj",
                KEY_EXPECTED: {
                    KEY_LENGTH: 1,
                    KEY_FIRST_WORD: "NickiMinaj",
                }
            },
            {
                KEY_INPUT: "Tupac Shakur",
                KEY_EXPECTED: {
                    KEY_LENGTH: 20,
                    KEY_FIRST_WORD: "biggie smalls",
                }
            },
            {
                KEY_INPUT: "Mondaona",
                KEY_EXPECTED: {
                    KEY_LENGTH: 3,
                    KEY_FIRST_WORD: "Mondona",
                }
            }

        ]
        self.exception_test_params=[
            {
                KEY_INPUT: 12,
            }
        ]


    def test_split_success(self):
        for test in self.success_test_params:
            inp = test[KEY_INPUT].split()
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(len(inp), expected[KEY_LENGTH])
            self.assertEqual(inp[0], expected[KEY_FIRST_WORD])
            self.assertEqual(inp[1], expected[KEY_SECOND_WORD])
            
    def test_split_failure(self):
        for test in self.failure_test_params:
            inp = test[KEY_INPUT].split()
            expected = test[KEY_EXPECTED]
            
            self.assertNotEqual(len(inp), expected[KEY_LENGTH])
            self.assertNotEqual(inp[0], expected[KEY_FIRST_WORD])
'''
    def test_split_exception(self):
        for test in self.exception_test_params:
            self.assertRaise(test[KEY_INPUT].split())
'''
if __name__ == '__main__':
    unittest.main()