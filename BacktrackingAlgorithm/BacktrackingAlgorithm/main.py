from Backtracking import Backtracking
from EinsteinP import EinsteinProblem
from ColorMapP import MapProblem


def main():
    einsteinProblem = EinsteinProblem()
    backtrackingEP = Backtracking(einsteinProblem)
    backtrackingEP.solve()

    x_size = 10
    y_size = 10
    points_length = 8
    k = 4
    mapProblem = MapProblem(x_size, y_size, points_length, k)
    backtrackingMP = Backtracking(mapProblem)
    backtrackingMP.solve()


if __name__ == "__main__":
    main()