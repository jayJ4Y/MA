import sqlite3
import pandas as pd

con = sqlite3.connect("DB/MaidanetskeBuildingsUsed2.sqlite")
cur = con.cursor()
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(res.fetchall())
cur.close()
df = pd.read_sql_query("SELECT GEOMETRY FROM maidanetskebuildingsused2", con)
r = df.xs(0)
print(r)