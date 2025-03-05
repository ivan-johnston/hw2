# =====================================================
# TestColorMaps01.py ...
# =====================================================

import matplotlib.pyplot as plt
import numpy as np

# main method ...

def main():
    print("--- Enter TestColorMaps01.main()             ... ");
    print("--- ======================================== ... ");

    # Create a 2x2 grid of subplots

    fig, axs = plt.subplots(2, 2, figsize=(10,10))

    # Generate random dataset for each subplot

    for i in range(2):
        for j in range(2):
            data = np.random.randn(100)
            axs[i, j].hist(data, color='red', alpha=0.5)
        
    # Apply a fancy colormap to the figure

    cmap = plt.get_cmap('hot')
    plt.set_cmap(cmap)

    # Show the figure

    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestColorMaps01.main()             ... ");

# call the main method ...

main()

