import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_get_winnier(self):
        board = [
            [ 'X', None, '0'],
            [None, 'X', None],
            [None, '0', 'X']
        ]

        self.assertEqual(logic.get_winner(board),'X')
    #TODO: Test All Functions from logic.py!
if __name__ == '__main__':
    unittest.main()