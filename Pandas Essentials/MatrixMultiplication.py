import numpy as np
import pandas as pd

a=[1,2,3,4,5]
b=[2,3,4,5,6]

mul = np.dot(a, b)
print(mul)


countries=['India', 'America', 'China', 'Russia', 'France', 'Brazil', 'Germany', 'England', 'Portugal']
gold= [9,8,7,6,5,4,3,2,1]
silver=[4,7,2,5,9,8,5,1,4]
bronze=[2,3,4,5,6,1,7,6,9]

olympics_medal_counts = {'country': pd.Series(countries), 'gold': pd.Series(gold), 'silver': pd.Series(silver), 'bronze': pd.Series(bronze)}
olympics_medal_counts_data_frame = pd.DataFrame(olympics_medal_counts)

print(olympics_medal_counts_data_frame[['gold', 'silver', 'bronze']])

medal_counts = olympics_medal_counts_data_frame[['gold', 'silver', 'bronze']]
points=np.dot(medal_counts, [4,2,1])

olympic_points = {'country' : pd.Series(countries), 'points' : pd.Series(points)}

print(pd.DataFrame(olympic_points))


