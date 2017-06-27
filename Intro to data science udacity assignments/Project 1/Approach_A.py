import pandas as pd

predictions = {}

df = pd.read_csv('train.csv')

for passenger_index, passenger in df.iterrows():
    sex = passenger['Sex']
    passenger_id = passenger['PassengerId']
    if sex == "female":
        predictions[passenger_id] = 1
    else :
        predictions[passenger_id] = 0

print(predictions)













