import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport
sns.set()

temperatures = pd.read_csv('files/data/temperatures-bordeaux-2009-2019.csv', usecols=['date', 'temperature'], parse_dates=['date'])

def generate_profile():
    profile = ProfileReport(temperatures)
    profile.to_file(output_file='files/data/exploration.html')

temperatures.plot(x='date', y='temperature')
plt.show()