import pandas as pd
import pandasql as pdsql

sample_aadhar = pd.read_csv('UIDAI-ENR-DETAIL-20170611.csv')

sample_data_frame = pd.DataFrame(sample_aadhar)
pysql = lambda q: pdsql.sqldf(q, globals())

sample_query =  """ select * from sample_data_frame where Registrar = 'Allahabad Bank' and District = 'Saharsa' """

result = pysql(sample_query)
print(result)
