import pandas as pd
import matplotlib as mpl
import numpy as np
import csv
import tables as tb
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as p
import seaborn as sns 
import matplotlib.pyplot as plt 
#plt.style.use('ggplot')
import scipy
import os
rootdir = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(rootdir +"/data_files/"+ "farm_data.csv", delimiter=",", header=0)

# I am defining two arrays for all the possible tests and operations
operations = ["Machine" , "Building", "Feed", "Indoor", "Treat", "Outdoor", "Feeding", "Milking", "Manure"]
tests = ["crush", "cut", "fall", "burn", "poison", "drown", "suffocate"]

def get_descriptive_summary(data_frame):
    #get information about the dataset
    print(data_frame.describe())
    #get counts in each category
    operation_counts = data["operation"].value_counts().to_frame()
    operation_counts.rename(columns={"operation":"value_counts"},inplace= True)
    #plot the boxplot vs fall
    fig, ax = plt.subplots()
    sns.boxplot(x="operation", y = "fall", data= data)
    plt.savefig(rootdir+"/output_files/fall_counts.png")
    #make a scatter plot to find a relation between fall and poison
    fig, ax = plt.subplots()
    sns.regplot(x = "fall",y= "poison", data =data)
    #plt.scatter(data["fall"], data["poison"])
   # plt.show()
    
    
def run_test_operation(target_respondant = False):
    get_descriptive_summary(data_frame = data )
    for operation in operations:
        # I will define a pdf file to include all the final plots
        pdf_file = rootdir +"/output_files/"+operation+'_output_results.pdf'
        Pdf = PdfPages(pdf_file)
        # Filter the data according to a specific  operation
        condition = (data["operation"] == operation)
        respondant = data[condition]  
         # return 4 bins of equal space over so that we can later use them for categorical analysis
        bins = np.linspace(min(respondant["crush"]), max(respondant["crush"]),4)
        crush_group_names =  ["Low", "Medium", "High"]
        #respondant["binned_data"] = pd.cut(respondant["crush"], bins, labels= crush_group_names, include_lowest= True)
        
        #convert categorical variables to dummy variables
        pd.get_dummies(respondant[target_respondant])
        
        test_array = []
        x = respondant[target_respondant]
        '''
        I will use a function called .corr() with the whole data to get the correlation matrix and plot it later 
        '''
        corr_matrix = np.array(respondant.corr(numeric_only = [False]).round(decimals=3))
        fig, ax = plt.subplots()
        im = ax.imshow(corr_matrix)
        im.set_clim(-1, 1)
        ax.grid(False)
        ax.xaxis.set(ticks=np.arange(len(tests)), ticklabels=tests)
        ax.yaxis.set(ticks=np.arange(len(tests)), ticklabels=tests)
        ax.set_ylim(len(tests)-0.5, -0.5)
        for i in range(len(tests)):
            for j in range(len(tests)):
                ax.text(j, i, corr_matrix[i, j], ha='center', va='center',color='r')
        cb = ax.figure.colorbar(im, ax=ax, format='% .2f')
        cb.set_label("r value")
        #ax.set_xlabel('Voltage [kV]')
        #ax.set_ylabel('Current [mA]')
        ax.set_title('correlation matrix for the whole survey', fontsize=12)   
        plt.xticks(rotation=45)
        plt.savefig(rootdir+"/output_files/"+operation+"_correlation_Matrix.png")
        Pdf.savefig()
        plt.close(fig)
        # loop over all the tests
        for test in tests:
            print("%i-%i plotting correlation between %s and %s for %s"%(operations.index(operation),tests.index(test), target_respondant,test, operation))
            y = respondant[test]
            '''
            I will use SciPy lib to extract the p-values and the correlation coefficients
            '''
            pearson_r, pearson_p = scipy.stats.pearsonr(x, y)  # Pearson's r
            Spearman_rho, Spearman_p = scipy.stats.spearmanr(x, y)  # Spearman's rho
            Kendall_tau, Kendall_p = scipy.stats.kendalltau(x, y)  # # Kendall's tau
            
            '''
            Visualization of Correlation
            '''
            slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)
            fig, ax = plt.subplots()
            # plot the data 
            label = 'Data points\n pearson_r'
            data_plot = ax.plot(x, y, linewidth=0, marker='s')
            # plot the regression line
            line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
            regression_plot = ax.plot(x, intercept + slope * x)
            # make a text box to show statistics
            ax.text(0.95, 0.80, "Pearson correlation: r =%0.3f, P-value = %0.3f\nSpearman correlation: rho=%0.3f, P-value = %0.3f\nKendall correlation:tau=%0.3f, P-value = %0.3f" % (pearson_r, pearson_p, Spearman_rho, Spearman_p, Kendall_tau, Kendall_p),
            horizontalalignment='right', verticalalignment='top', transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            ax.set_title('correlation result between %s and %s data'%(target_respondant,test), fontsize=12)             
            ax.set_xlabel(target_respondant)
            ax.set_ylabel(test)
            ax.legend(["Data correlation", line], facecolor='white')
            #plt.savefig(rootdir +"/output_files/"+operation+"_correlation_"+test+".png")
            Pdf.savefig()
            plt.close(fig)
    Pdf.close()

                
                
                
if __name__ == '__main__':
    run_test_operation(target_respondant = "crush")
    
    
    
    
    