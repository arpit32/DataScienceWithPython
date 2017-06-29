import pandas
cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
cols.remove('PassengerId')
cols.remove('Survived')
cols.remove('Name')
# Ticket?
cols.remove('Ticket')

# Bucketize age
df = pandas.read_csv('train.csv')
df['Age'].fillna(-1, inplace=True)
df['AgeBucket'] = pandas.Series('', index=df.index)
for idx, row in df.iterrows():
    age = row['Age']
    age_bucket = 'c'
    if age < 18:
        age_bucket = 'young'
    elif age < 25:
        age_bucket = 'midyoung'
    elif age < 40:
        age_bucket = 'midmid'
    else:
        age_bucket = 'old'
    df.loc[idx, 'AgeBucket'] = age_bucket
    # After AgeBucket is added, replace the Age with Bucket
cols.remove('Age')
cols.append('AgeBucket')

# Replace cabin with first char
df['Deck'] = pandas.Series('', index=df.index)
for idx, row in df.iterrows():
    cabin = row['Cabin']
    if not pandas.isnull(cabin):
        df.loc[idx, 'Deck'] = cabin[0]
cols.remove('Cabin')
cols.append('Deck')

# Bucketize fare
df['Fare'].fillna(-1, inplace=True)
df['FareBucket'] = pandas.Series(0, index=df.index)
for idx, row in df.iterrows():
    fare = row['Fare']
    # Cap to makes bucketizing look nicer
    if fare > 100:
        df.loc[idx, 'Fare'] = 100

    fare_bucket = ''
    if fare <= 10:
        fare_bucket = 10
    elif fare <= 20:
        fare_bucket = 20
    elif fare <= 30:
        fare_bucket = 30
    elif fare <= 40:
        fare_bucket = 40
    else:
        fare_bucket = 100
    df.loc[idx, 'FareBucket'] = fare_bucket
cols.remove('Fare')
cols.append('FareBucket')

# Print data relations
features = []
for i, coli in enumerate(cols):
    for j, colj in enumerate(cols):
        if i <= j:
            features.append([coli, colj])
            # features.append([coli, colj, 'Sex'])
    print(features)
features = []
#x = df[(df['Sex'] == 'male') & (df['Deck'] == 'E') & (df['AgeBucket'] == 'midmid')]
# print(df)
survivor_threshold = 0.8
base_threshold = 0
for f in features:
            print("--------------------------------------------------------------")
            print(f)
            predictions = {}

            for passenger_index, passenger in df.iterrows():
                key = ''
                for k in f:
                    v = passenger[k]
                key = key + ' ' + str(v)

            predictions.setdefault(key, [0, 0])
            predictions[key][0] += passenger['Survived']
            predictions[key][1] += 1

            # Print the stats for features list
            # print ', '.join(df.columns)
            # print predictions
            for k in sorted(predictions.keys()):
                v = predictions[k]
                survivor = 1.0 * v[0] /  v[1]
                base = v[1]
                if survivor < survivor_threshold or base < base_threshold or 'female' in k:
                    continue
                print ('%s => %.2f (%d)' % (k, (1.0 * v[0] /  v[1]), v[1]))

# Observations:
# PREDICTION female in [1, 2] class => 97, 92%
# PREDICTION female with SbSp <= 2 [0.79, 0.75, 0.77]
# PREDICTION female not from S [69%, against C, Q]
# PREDICTION decks: B, D, E
# TODO: fare: bucketize


total_survivors = 0
predictions = {}
# df = pandas.read_csv(file_path)
for passenger_index, passenger in df.iterrows():
    passenger_id = passenger['PassengerId']
    survivor = 0

    sex = passenger['Sex']
    if sex == 'female':
        # 1 or 2nd class?
        if passenger['Pclass'] in [1, 2]:
            survivor = 1
        # Embarked in 'C' (Cherbourg)?
        if passenger['Embarked'] == 'C':
            survivor = 1
        if passenger['Deck'] in ['B', 'C', 'D', 'E']:
            survivor = 1
        if passenger['FareBucket'] == 100:
            survivor = 1

    # Bunch of findings
    if passenger['Pclass'] == 2 and passenger['Parch'] == 2:
        survivor = 1
    if passenger['SibSp'] == 1 and passenger['Deck'] in ['B', 'D']:
        survivor = 1
    if passenger['Parch'] == 2 and passenger['AgeBucket'] == 'midyoung':
        survivor = 1
    if passenger['Embarked'] == 'C' and passenger['Deck'] == 'D':
        survivor = 1
    if passenger['AgeBucket'] == 'midmid' and passenger['Deck'] in ['B', 'D']:
        survivor = 1
    if passenger['Sex'] == 'male' and passenger['Deck'] in ['E'] and passenger['AgeBucket'] == 'midmid':
        survivor = 1



    predictions[passenger_id] = survivor
    if survivor:
        total_survivors = total_survivors + 1

print ('prediction rate: ', total_survivors, len(predictions))
accurate = 0
for _, passenger in df.iterrows():
    passenger_id = passenger['PassengerId']
    prediction = predictions[passenger_id]
    if prediction == passenger['Survived']:
        accurate = accurate + 1
#survived = sum(df['Survived'] == 1)
print ('accuracy: ', (1.0 * accurate / len(predictions)))

print(predictions)