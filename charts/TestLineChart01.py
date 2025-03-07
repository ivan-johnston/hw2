# =====================================================
# TestLineChart01.py ....
# =====================================================

import matplotlib.pyplot as plt

# main method ...

def main():
    print("--- Enter TestLineChart01.main()             ... ");
    print("--- ======================================== ... ");

    x  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y1 = [1, 3, 5, 3, 1, 3, 5, 3, 1]
    y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]

    plt.plot(x, y1, label="line L")
    plt.plot(x, y2, label="line H")
    plt.plot()

    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title("Line Graph Example")
    plt.legend()
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestLineChart01.main()             ... ");

# call the main method ...

main()

