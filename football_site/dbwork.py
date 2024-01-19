import sqlite3
import pandas as pd
from datetime import datetime
def execute_query(query, variables):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    if variables:
        cursor.execute(query, variables)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

df = pd.read_json('match_data.json')
playoff_df = df.loc[48:].copy()
print(playoff_df.columns)
print(playoff_df.dtypes)
dtypes_dict = {'int64':'INTEGER',
          'float64':'FLOAT',
          'object':'VARCHAR(255)',
          'datetime64[ns]':'datetime'}

# query = 'CREATE TABLE match_data(matchid INTEGER'
# for i, column in enumerate(playoff_df.columns):
#     query+=f', {column} {dtypes_dict[str(playoff_df.dtypes[i])]}'
# query += ');'
# print(query)
# execute_query(query, [])
# matches = df.to_dict('records')
print(df['home_formation'].unique())
print(df['away_formation'].unique())

# for match in matches:
#     print(match)
#     match['match_time'] = str(match['match_time'])
#     query = f"""INSERT INTO match_data({', '.join(column for column in df.columns.values)})
#                 VALUES ({', '.join('?' for i in range(len(df.columns.values)))});"""
#     print(tuple(match.values()))
#     execute_query(query, tuple(match.values()))
