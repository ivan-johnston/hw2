

# =====================================================
# TestScatter2D.py .....
# =====================================================

import matplotlib.pyplot as plt

# main method ...

def main():
    print("--- Enter TestScatter2D.main()               ... ");
    print("--- ======================================== ... ");

    x1 = [2, 3, 4]
    y1 = [5, 5, 5]

    x2 = [1, 2, 3, 4, 5]
    y2 = [2, 3, 2, 3, 4]
    y3 = [6, 8, 7, 8, 7]

    # Markers: https://matplotlib.org/api/markers_api.html

    plt.scatter(x1, y1)
    plt.scatter(x2, y2, marker='v', color='r')
    plt.scatter(x2, y3, marker='^', color='m')
    plt.title('Scatter Plot Example')
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestScatter2D.main()               ... ");

# call the main method ...

main()

