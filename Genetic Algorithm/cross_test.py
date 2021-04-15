import unittest

from Chromosome import *
from cross import onePointCrossover

class TestCrossingMethods(unittest.TestCase): 
    f_path_segments_1 = [Segment('up', 3)]
    f_path_segments_2 = [Segment('down', 1)]
    f_path_segments_3 = [Segment('left', 5)]
    f_path_segments_4 = [Segment('right', 2)]

    father_paths = [Path(Point(1,1), Point(1,1),f_path_segments_1 ),
                    Path(Point(2,2), Point(2,2),f_path_segments_2 ),
                    Path(Point(3,3), Point(3,3),f_path_segments_3 ),
                    Path(Point(4,4), Point(4,4),f_path_segments_4 )]

    father = Chromosome(father_paths)

    m_path_segments_1 = [Segment('left', 3)]
    m_path_segments_2 = [Segment('right', 1)]
    m_path_segments_3 = [Segment('up', 5)]
    m_path_segments_4 = [Segment('down', 2)]

    mother_paths = [Path(Point(1,1), Point(1,1),m_path_segments_1 ),
                    Path(Point(2,2), Point(2,2),m_path_segments_2 ),
                    Path(Point(3,3), Point(3,3),m_path_segments_3 ),
                    Path(Point(4,4), Point(4,4),m_path_segments_4 )]

    mother = Chromosome(mother_paths)

    def testOnePointCrossoverFirst(self):
        child_1, child_2 = onePointCrossover(self.mother, self.father, 0)

        assert child_1.paths == [Path(Point(1,1), Point(1,1),self.m_path_segments_1 ),
                    Path(Point(2,2), Point(2,2), self.f_path_segments_2 ),
                    Path(Point(3,3), Point(3,3), self.f_path_segments_3 ),
                    Path(Point(4,4), Point(4,4), self.f_path_segments_4 )]

        assert child_2.paths == [Path(Point(1,1), Point(1,1),self.f_path_segments_1 ),
                    Path(Point(2,2), Point(2,2),self.m_path_segments_2 ),
                    Path(Point(3,3), Point(3,3),self.m_path_segments_3 ),
                    Path(Point(4,4), Point(4,4),self.m_path_segments_4 )]

    def testOnePointCrossoverSecond(self):
        child_1, child_2 = onePointCrossover(self.mother, self.father, 2)

        assert child_1.paths == [Path(Point(1,1), Point(1,1),self.m_path_segments_1 ),
                    Path(Point(2,2), Point(2,2), self.m_path_segments_2 ),
                    Path(Point(3,3), Point(3,3), self.m_path_segments_3 ),
                    Path(Point(4,4), Point(4,4), self.f_path_segments_4 )]

        assert child_2.paths == [Path(Point(1,1), Point(1,1), self.f_path_segments_1 ),
                    Path(Point(2,2), Point(2,2), self.f_path_segments_2 ),
                    Path(Point(3,3), Point(3,3), self.f_path_segments_3 ),
                    Path(Point(4,4), Point(4,4), self.m_path_segments_4 )]

    def testOnePointCrossoverIllegalValue(self):
        try:
            child_1, child_2 = onePointCrossover(self.mother, self.father, -3)
        except ValueError:
            assert True == True
        else:
            raise AssertionError("ValueError was not raised")


if __name__ == '__main__':
    unittest.main()