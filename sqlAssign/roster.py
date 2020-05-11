import json
import sqlite3


class RosterData:
    con = sqlite3.connect("rosterDB.sqlite")
    cur = con.cursor()

    cur.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Course;
        DROP TABLE IF EXISTS Member;
        
        CREATE TABLE User (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
            name varchar(255)
        );
        
        CREATE TABLE Course (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE ,
            title varchar(255)
        );
        
        CREATE TABLE Member (
            user_id INTEGER,
            course_id INTEGER,
            role INTEGER ,
            PRIMARY KEY (user_id,course_id)
        );
    ''')
    con.commit()

    with open('roster_data.json', 'r') as file:
        loaded_json = json.loads(file.read())

        for row in loaded_json:
            user = row[0]
            title = row[1]
            role = row[2]

            cur.execute('''
                INSERT OR IGNORE INTO User(name) VALUES (?)
            ''', (user,))
            cur.execute('''
                SELECT id FROM USER WHERE name= ?
            ''', (user,))
            user_id = cur.fetchone()[0]

            cur.execute('''
                INSERT OR IGNORE INTO Course(title) VALUES (?)
            ''', (title,))
            cur.execute('''
                SELECT id FROM Course WHERE title= ?
            ''', (title,))
            course_id = cur.fetchone()[0]

            cur.execute('''
                INSERT OR IGNORE INTO Member(user_id,course_id,role) VALUES (?,?,?)
            ''', (user_id, course_id, role))

    con.commit()
    con.close()
