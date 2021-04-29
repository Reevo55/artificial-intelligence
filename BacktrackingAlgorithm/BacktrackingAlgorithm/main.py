from Backtracking import Backtracking
from EinsteinP import EinsteinProblem
from ColorMapP import MapProblem
from ForwardChecking import ForwardChecking
from ValueChoser import *
from VariableChoser import *
import copy
import matplotlib.pyplot as plt
import time

x_size = 12
y_size = 12
points_length = 8
k = 4


def draw_plots(backtracking, foward, N_arr, xname, yname, title):
    plt.plot(N_arr, backtracking)
    plt.plot(N_arr, foward)

    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)

    plt.legend(["Backtracking", "FowardChecking"])

    plt.show()


def research(N):
    backtracking_nodes = []
    foward_nodes = []
    backtracking_time = []
    foward_time = []
    N_arr = []

    mapProblem = None
    backtracking = None
    foward = None
    # Value
    nvc = NextValueChooser()
    lcvc = LeastConstrainedValueChooser()

    # Variable
    nvlc = NextVariableChooser()
    mcvc = MostConstrainedVariableChooser()

    for i in range(2, N):
        print("Evaluating... [" + str(i) + "]")
        mapProblem = None
        backtracking = None
        foward = None

        mapProblem = MapProblem(x_size, y_size, i, k, mcvc, lcvc)
        print("Backtracking")
        backtracking = Backtracking(copy.deepcopy(mapProblem))
        print("FowardChecking")
        foward = ForwardChecking(copy.deepcopy(mapProblem))

        print("Backtracking solve")
        b_nodes, b_time = timer(backtracking.solve_one)
        print("Backtracking solve")
        f_nodes, f_time = timer(foward.solve_one)

        backtracking_nodes.append(b_nodes)
        backtracking_time.append(b_time)
        foward_nodes.append(f_nodes)
        foward_time.append(f_time)
        N_arr.append(i)

    print("Backtracking nodes")
    print(backtracking_nodes)
    print("Backtracking time")
    print(backtracking_time)

    print("Foward nodes")
    print(foward_nodes)
    print("Foward time")
    print(foward_time)

    # Nodes
    draw_plots(backtracking_nodes, foward_nodes, N_arr, "N", "Visited", "Comparison")
    # Time
    draw_plots(foward_time, backtracking_time, N_arr, "N", "Time", "Comparison")


def timer(func):
    start = time.time()
    var = func()
    end = time.time()

    return (var, end - start)


def main():
    # research(12)
    # Value
    nvc = NextValueChooser()
    lcvc = LeastConstrainedValueChooser()

    # Variable
    nvlc = NextVariableChooser()
    mcvc = MostConstrainedVariableChooser()

    einsteinProblem = EinsteinProblem(mcvc, lcvc)
    # einsteinProblem = EinsteinProblem(mcvc, lcvc)
    # mapProblem = MapProblem(x_size, y_size, points_length, k, nvlc, nvc)

    print("====== BACKTRACKING =================================")
    print("--- EINSTEIN ---")
    fc = ForwardChecking(copy.deepcopy(einsteinProblem))
    b_nodes, b_time = timer(fc.solve_all)
    print("fc nodes")
    print(b_nodes)
    print("fc time")
    print(b_time)

    # foward = ForwardChecking(copy.deepcopy(einsteinProblem))
    # print(foward.solve_all())


if __name__ == "__main__":
    main()