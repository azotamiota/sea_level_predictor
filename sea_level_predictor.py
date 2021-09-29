import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
plt.rcParams['figure.facecolor'] = 'lightblue'
plt.rcParams['axes.facecolor'] = 'lightgrey'

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='red')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    yearpr = pd.Series(i for i in range(1880, 2051))
    plt.plot(yearpr, intercept + slope * yearpr, 'blue', label='best fit')

    # Create second line of best fit
    df_2000 = df[df['Year'] > 1999]
    slope2, intercept2, r_value2, p_value2, std_err2 = scipy.stats.linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    yearpr2 = pd.Series(i for i in range(2000, 2051))
    plt.plot(yearpr2, intercept2 + slope2 * yearpr2, 'pink', label='updated best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
