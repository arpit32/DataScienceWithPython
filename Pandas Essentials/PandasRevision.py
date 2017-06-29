#creating a data frame usnig dict of dicts and then transposing the created data frame
import pandas as pd

# data = pd.DataFrame({0: {'patient': 1, 'phylum': 'Firmicutes', 'value': 632},
#                   1: {'patient': 1, 'phylum': 'Proteobacteria', 'value': 1638},
#                     2: {'patient': 1, 'phylum': 'Actinobacteria', 'value': 569},
#                     3: {'patient': 1, 'phylum': 'Bacteroidetes', 'value': 115},
#                     4: {'patient': 2, 'phylum': 'Firmicutes', 'value': 433},
#                     5: {'patient': 2, 'phylum': 'Proteobacteria', 'value': 1130},
#                     6: {'patient': 2, 'phylum': 'Actinobacteria', 'value': 754},
#                     7: {'patient': 2, 'phylum': 'Bacteroidetes', 'value': 555}})
# result = data.T
# print(data.T)
#
# print(data.T.value[2])
#
# treatment = pd.Series([0]*4 + [1]*2)
# result['treatment'] = treatment
#
# print(result)
#
# microbiome_data = pd.read_csv('microbiome.csv')
# microbiome_df = pd.DataFrame(microbiome_data)
# print(microbiome_df)
#
# #some misclleneous operations that can be performed upon a csv file
#
# microbiome_data = pd.read_csv('microbiome.csv', header = None) # implies that header will also be considered while processing the csv file
# print(pd.DataFrame(microbiome_data))
#
# # microbiome_data = pd.read_csv('microbiome.csv', chunksize = 15)
# # mean_tissue = {chunk.Taxon[0]:chunk.Tissue.mean() for chunk in microbiome_data}
# # print(mean_tissue)

baseball_data = pd.read_csv('baseball.csv', index_col = 'id')
# print(baseball_data.head())

player_id = baseball_data.player + baseball_data.team + baseball_data.year.astype(str)
baseball_data_new = baseball_data.copy()
baseball_data_new.index=player_id
# print(baseball_data_new.head())
#
# print(baseball_data_new.index.is_unique)

#operations on data frame

hr2006 = baseball_data[baseball_data.year==2006].xs('hr', axis=1)
# print(hr2006)
# hr2006.index = baseball_data.player[baseball_data.year==2006]

hr2006 = pd.Series(baseball_data.hr[baseball_data.year==2006].values, index = baseball_data.player[baseball_data.year==2006].values)
hr2007 = pd.Series(baseball_data.hr[baseball_data.year==2007].values, index =  baseball_data.player[baseball_data.year==2007].values)
# print(hr2006)
# print(hr2007)
# print(hr2006+hr2007)
# print((hr2006+hr2007)[(hr2006+hr2007).notnull()])

# print(hr2007.add(hr2006, fill_value=0))
# print(hr2007)
# print(baseball_data[baseball_data.player=='finlest01'])

stats = baseball_data[['h', 'X2b', 'X3b', 'hr']]
diff = stats - stats.xs(89521)
# print(diff[:10])




