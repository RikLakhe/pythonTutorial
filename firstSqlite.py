import sqlite3
import re


class emailCount:
    con = sqlite3.connect('assignment.sqlite')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS Counts')
    cur.execute('CREATE TABLE IF NOT EXISTS Counts (org TEXT,count INTEGER )')
    con.commit()
    with open('mbox.txt', 'r') as fn:
        for line in fn:
            if not line.startswith('From: '): continue
            domain = line.split('@')[1]
            print('gere', domain)
            cur.execute('SELECT * FROM Counts WHERE org = ?', (domain,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
        con.commit()

        for row in con.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'):
            # for row in con.execute('SELECT * FROM Counts '):
            print(str(row[0]), row[1])

        con.close()
