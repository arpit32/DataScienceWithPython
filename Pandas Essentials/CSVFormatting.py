import pandas as pd

sample_data=pd.read_csv('BP_Output.csv')

df=pd.DataFrame(sample_data)
# print(df)

# if we wished to concatnate all the address columns into one single column
df['FULL_ADDRESS'] = df['ADDRESS_ADDON'] + df['ADDRESS_ADDON2'] + df['ADDRESS_ADDON3']

print(df)