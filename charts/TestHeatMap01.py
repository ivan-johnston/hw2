# =====================================================
# TestHeatMap01.py ...
# =====================================================

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# main method ...

def main():
    print("--- Enter TestHeatMap01.main()               ... ");
    print("--- ======================================== ... ");

    # Create a dataset

    data = 100*np.random.random(size=(9,7))

    np.set_printoptions(precision=2)
    print(data)

    # Insert data into pandas dataframe ...

    df = pd.DataFrame( data )

    # Change the column names and row indexes ...

    df.columns = [   "Mon",  "Tue",  "Wed","Thu","Fri","Sat", "Sun"]
    df.index   = ["12-1am","1-2am","2-3am","3-4am","4-5am","5-6am","6-7am","7-8am","8-9am"]

    # Default heatmap with active annotations ...

    p1 = sns.heatmap(df, annot=True, fmt=".1f")

    # This sets the yticks "upright" with 0, as opposed to sideways with 90.

    plt.yticks(rotation=0)
    plt.title("Heatmap of weekly measurements")
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestHeatMap01.main()               ... ");

# call the main method ...

main()

