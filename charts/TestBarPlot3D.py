# =====================================================
# TestBarPlot3D.py ...
# =====================================================

import matplotlib.pyplot as plt
import numpy as np

# main method ...

def main():
    print("--- Enter TestBarPlot3D.main()     ... ");
    print("--- ======================================== ... ");

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = np.random.randint(10, size=10)
    z = np.zeros(10)

    dx = np.ones(10)
    dy = np.ones(10)
    dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    ax.bar3d(x, y, z, dx, dy, dz, color='g')

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    plt.title("3D Bar Chart Example")
    plt.tight_layout()
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestBarPlot3D.main()     ... ");

# call the main method ...

main()

