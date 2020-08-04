import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport
sns.set()

temperatures = pd.read_csv('files/data/temperatures-bordeaux-2009-2019.csv', usecols=['date', 'temperature'], parse_dates=['date'])

def generate_profile():
    profile = ProfileReport(temperatures)
    profile.to_file(output_file='files/data/exploration.html')

temperatures['year'] = temperatures['date'].dt.year
temperatures['year'] = temperatures['year'].astype('category')

temperatures_per_year = temperatures.groupby('year')

for year, df in temperatures_per_year:
    plt.plot(df['date'], df['temperature'], label = 'Année '+ str(year))

plt.xlabel('Date')
plt.ylabel('Température (°C)')
plt.suptitle('Evolution de la Température sur Bordeaux, France (2009-2019)')
plt.title('Sources: https://www.historique-meteo.net/', y=0, fontsize=10)

plt.show()

plt.clf()
