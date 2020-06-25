
import challenges
import unittest


class NumIslandsTests(unittest.TestCase):
    def test_numIslands(self):
        """Returns the number of distinct land masses from a 2D grid."""
        # Test Cases
        map1 = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        assert challenges.numIslands(map1) == 1

        map2 = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        assert challenges.numIslands(map2) == 3


if __name__ == '__main__':
    unittest.main()