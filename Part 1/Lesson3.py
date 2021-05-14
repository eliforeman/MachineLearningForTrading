#%%
import pandas as pd

df = pd.read_csv("../Resources/data/YHOO.csv")


start_date = '2004-10-20'
end_date = '2004-10-31'

dates = pd.date_range(start_date,end_date)

#print(dates[0])

#new dataframe with dates as index
df1 = pd.DataFrame(index=dates)
print(df1)


