import unittest
from Chromosome import *
from mutation import mutatePath
import copy

class TestCrossingMethods(unittest.TestCase): 
    segments_1 = Segment('up', 3)
    segments_2 = Segment('right', 1)
    segments_3 = Segment('down', 3)
    segments_4 = Segment('right', 2)


    segments = []
    segments.append(segments_1)
    segments.append(segments_2)
    segments.append(segments_3)
    segments.append(segments_4)


    path = Path(Point(1,1), Point(2,2), segments)

    def testMutation_up(self):
        mutated =  copy.deepcopy(self.path)
        mutatePath(mutated, 0)

        assert mutated == Path(Point(1,1), Point(2,2), [Segment('up', 4), Segment('right', 1), Segment('down', 2), Segment('right', 2)])

    def testMutation_right(self):
        mutated =  copy.deepcopy(self.path)
        mutatePath(mutated, 1)

        assert mutated == Path(Point(1,1), Point(2,2), [Segment('up', 3), Segment('right', 2), Segment('down', 3), Segment('right', 1)])

if __name__ == '__main__':
    unittest.main()