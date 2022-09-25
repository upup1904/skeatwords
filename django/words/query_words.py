import sqlite3
import pathlib

sqlite_file = pathlib.Path("/tmp") / "letssee.sqlite"

conn = sqlite3.connect(sqlite_file.absolute())

query_template = """
select min(word), 'NEXT' as rel from wordlist 
	where word > '{target}'
UNION
select max(word), 'PREV' as rel from wordlist 
	where word < '{target}'
;
"""
cur = conn.cursor()
cur.execute(query_template.format(target='earthsophagus'))

for x in cur:
    print(x)
