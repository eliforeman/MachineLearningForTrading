#%%
import pandas as pd
import matplotlib.pyplot as plt


aapl = "/Users/eliforeman/Desktop/Machine Learning For Trading/Resources/data/AAPL.csv"
goog = "/Users/eliforeman/Desktop/Machine Learning For Trading/Resources/data/GOOG.csv"
 
df = pd.read_csv(aapl);

# Max close
maxClose = df['Close'].max()
print(maxClose)

#mean vol
def getMeanVal(symbol):
    df = pd.read_csv("/Users/eliforeman/Desktop/Machine Learning For Trading/Resources/data/{}.csv".format(symbol))
    meanVol = df['Volume'].mean()
    return symbol, meanVol
print(getMeanVal('AAPL'))

def showGraph(symbol):
    df = pd.read_csv("/Users/eliforeman/Desktop/Machine Learning For Trading/Resources/data/{}.csv".format(symbol))
    df[['High','Volume']].plot()
    plt.show()
showGraph('IBM')





