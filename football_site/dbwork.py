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

df = pd.read_json('sankey_data3.json')
print(df)
df = df.rename(columns={'Team Strategy':'team_strategy'})
print(df.columns)
print(set(df.dtypes))
dtypes_dict = {'int64':'INTEGER',
          'float64':'REAL',
          'object':'TEXT',
          'datetime64[ns]':'datetime'}

query = 'CREATE TABLE sankey_data(teamid INTEGER'
for i, column in enumerate(df.columns):
    query+=f', {column} {dtypes_dict[str(df.dtypes[i])]}'
query += ');'
print(query)
execute_query(query, [])
teams = df.to_dict('records')
# print(df['home_formation'].unique())
# print(df['away_formation'].unique())

for team in teams:
    print(team)
    query = f"""INSERT INTO sankey_data({', '.join(column for column in df.columns.values)})
                VALUES ({', '.join('?' for i in range(len(df.columns.values)))});"""
    print(tuple(team.values()))
    execute_query(query, tuple(team.values()))
