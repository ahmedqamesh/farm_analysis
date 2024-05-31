# Farm Analysis Script
This script is dedicated to conducting analysis and statistical calculations, such as p-values and correlation coefficients, on real data collected from a farm in 2021.

## Overview
The script follows the following workflow:
1. **Data Loading**: Load the dataset.
2. **Data Filtering**: Filter the dataset based on the target operation.
3. **Operation Looping**: Iterate over all operations included in the array `operations`.
4. **Analysis for Each Operation**:
    - Use the `.corr()` function with the whole data to obtain the correlation matrix and plot it.
    - Utilize SciPy library to extract p-values and correlation coefficients for each combination between "crush" and the tests.
    - Plot the results and display the p-value, Pearson correlation coefficient (r), Spearman correlation coefficient (rho), and Kendall correlation coefficient (tau).
    - Save the plots individually with .png extension and generate a separate PDF file per operation to consolidate all results.

## Installation and Usage
1. **Clone Repository**: Clone the repository to obtain the source code.
```
git@github.com:ahmedqamesh/farm_analysis.git
```
2. **Run the Script**: Run the following command in the home directory:
```
python run_test.py
```

## Contributing and Contact Information:
We welcome contributions from the community please contact : `ahmed.qamesh@gmail.com`.
