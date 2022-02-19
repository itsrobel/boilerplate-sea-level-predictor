from cv2 import line
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file

    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)
    # Create first line of best fit
    years_extended = np.arange(1880, 2051, 1)

    y = pd.Series(df['CSIRO Adjusted Sea Level'])
    x = pd.Series(df['Year'])

    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    line = [slope*xi + intercept for xi in years_extended]

    plt.plot(years_extended, line, color='orange',
             label="Fitting Line", linewidth=1)

    years_extended_2 = np.arange(2000, 2051, 1)

    # y_2 = pd.Series(df['CSIRO Adjusted Sea Level'])
    # x_2 = pd.Series(df['Year'])

    df_2000 = df[df['Year'] >= 2000]

    line = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    # x = np.arange(2000, 2051, 1)
    y = years_extended_2*line.slope + line.intercept

    plt.plot(years_extended_2, y)
    # slope_2, intercept_2, r_value, p_value, std_err = linregress(x, y)

    # line_2 = [slope_2*xi + intercept_2 for xi in years_extended_2]

    # plt.plot(years_extended_2, line_2, color='pink',
    #          label="Fitting Line", linewidth=1)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.savefig('sea_level_plot.png')
    return plt.gca()
