This script is dedicated for some analysis and statistical calculations (e.g. p-values and the correlation coefficients). <br>
The data set: is a real data collected from a farm in 2021.  <br>
The script works as follow:<br>
i- it loads the data <br>
ii - filter it based on the target operation. <br>
iii -  it loops over all the operations included in the array
operations = ["Machine" , "Building", "Feed", "Indoor", "Treat", "Outdoor", "Feeding", "Milking", "Manure"] <br>
iv: for each operation it will make the following : <br>
a) use a function called .corr() with the whole data to get the correlation matrix and plot it 
b)  use SciPy lib to extract the p-values and the correlation coefficients for each combination between "crush" and  tests = [, "cut", "fall", "burn", "poison", "drown", "suffocate"] <br>
c) plot the result in a plot and show the p-value and r , rho, tau using Pearson, Spearman and Kendall. <br>
d) the plots will be saved individually with .png extension and also you will find a separate pdf file per operation so that all your results will be in one place. <br>


## Dependencies
All third-party Python packages that are needed can be found on the [Twiki](https://gitlab.cern.ch/aqamesh/canmops/-/wikis/home) page. The necessary AnaGate libraries are also included in this repository. For the use of Kvaser CAN interfaces you have to install the [Kvaser drivers](https://www.kvaser.com/downloads-kvaser/ "Kvaser download page") first which are avaiable for [Windows](https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130980013&utm_status=latest) and [Linux](https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130980754&utm_status=latest).

### Installation and usage
Clone the repository to get a copy of the source code (for developers):

```
git@github.com:ahmedqamesh/farm_analysis.git
```

Make sure that the CAN interface is connected and the needed software is installed.
Simply in the home directory run:

```
python run_test.py
```

