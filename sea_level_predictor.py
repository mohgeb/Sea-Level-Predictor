import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv('/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv')

plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

years_extended = pd.Series(range(1880, 2051))
line_full = intercept + slope * years_extended

plt.plot(years_extended, line_full, label="Full Dataset Best Fit", color='red')

recent_data = data[data['Year'] >= 2000]

slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

line_recent = intercept_recent + slope_recent * years_extended

plt.plot(years_extended, line_recent, label="2000 Onward Best Fit", color='green')

plt.legend()
plt.grid(True)
plt.savefig('/workspace/boilerplate-sea-level-predictor/sea_level_rise.png')
plt.show()
