import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('.venv/911.csv')


df.columns = df.columns.str.lower()


df['reason'] = df['title'].apply(lambda title: title.split(':')[0])

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['month'] = df['timestamp'].apply(lambda time: time.month)
df['Hour']=df['timestamp'].apply(lambda time:time.hour)
df['day of week'] = df['timestamp'].apply(lambda day: day.dayofweek)

dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
df['day of week'] = df['day of week'].map(dmap)

dayHour=df.groupby(by=['day of week','Hour']).count()['reason'].unstack()
sns.heatmap(dayHour,cmap='viridis')
plt.grid(True)
plt.tight_layout()

plt.show()
