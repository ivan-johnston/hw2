# =====================================================
# TestPieChart01.py ....
# =====================================================

import matplotlib.pyplot as plt

# main method ...

def main():
    print("--- Enter TestPieChart01.main()              ... ");
    print("--- ======================================== ... ");

    labels = 'S1', 'S2', 'S3'
    sections = [56, 66, 24]
    colors = ['c', 'g', 'y']

    # Assemble pie chart model ...

    plt.pie(sections, labels=labels, colors=colors,
            startangle=90,
            explode = (0, 0.1, 0),
            autopct = '%1.2f%%')

    # Label and show pie chart ...

    plt.axis('equal') # Try commenting this out.
    plt.title('Pie Chart Example')
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestPieChart01.main()              ... ");

# call the main method ...

main()
