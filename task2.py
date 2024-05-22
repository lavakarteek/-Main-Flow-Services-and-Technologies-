import pandas as pd
df=pd.read_csv("details (2).csv")

#loading data
r,c=df.shape
print(df.head(r))
#filtering data
filt=df[df["BlowFlow"]==121.717]
print(filt)
print(df.dtypes)
#handling missing values
df.info()
df.fillna(0,inplace=True)
df.info()
#summary statistics
summary_info=df.describe()
print(summary_info)