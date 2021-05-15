#%%
import pandas as pd

df = pd.read_csv("../Resources/data/YHOO.csv")


start_date = '2010-01-22'
end_date = '2010-01-31'

dates = pd.date_range(start_date,end_date)

#print(dates[0])

#new dataframe with dates as index
df1 = pd.DataFrame(index=dates)
dfSPY = pd.read_csv('../Resources/data/SPY.csv', index_col='Date',parse_dates=True) 

print(df1.join(dfSPY))


