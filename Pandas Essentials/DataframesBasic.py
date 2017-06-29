import pandas as pd
import numpy as np

d = {'name' : pd.Series(['arpit', 'shubham', 'shivam', 'duvuru'], index=['1', '2', '3', '4']), 'age' : pd.Series([22,23,24,25],
    index=['1', '2', '3', '4']), 'height' : pd.Series(['5.8', '5.5', '5.8', '5.10'],  index=['1', '2', '3', '4']), 'Survivor' : pd.Series([True, False, True, False],  index=['1', '2', '3', '4'])}

df= pd.DataFrame(d)

print(df[['name', 'age']])
print(df.loc['1'])
print(df[df['age']<=24])

print(df['age'].apply(np.mean))

print(df['age'].map(lambda x: x >= 23))
