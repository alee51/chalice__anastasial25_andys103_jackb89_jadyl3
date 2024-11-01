# Chalice: Anastasia, Andy, Jack, Jady
# SoftDev
# October 2024

import sqlite3 #enable SQLite operations

DB_FILE="stories.db"
#open db if exists, otherwise create
db = sqlite3.connect(DB_FILE) 
c = db.cursor() #facilitate db ops

# storiesDontExist = (c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stories'").fetchall() == [])
# if storiesDontExist:
#     command = "CREATE TABLE IF NOT EXISTS stories (story_id INT AUTO_INCREMENT PRIMARY KEY, story_name)"
#     c.execute(command)
command = "CREATE TABLE IF NOT EXISTS stories (story_id INT PRIMARY KEY, story_name text NOT NULL, authors, chapters)"
c.execute(command)
command = "CREATE TABLE IF NOT EXISTS chapters (story_id INT, content text NOT NULL, author, date)"
c.execute(command)
# """CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name text NOT NULL, begin_date DATE, end_date DATE);"""

# call whenever user adds a story. 
# story_name, author, first_chapter, and date should all be strings.
def addStory(story_name, author, first_chapter, date):
    # create story table
    command = "INSERT INTO stories (story_name) VALUES (?)"
    val = (story_name,)
    c.execute(command, val)
    db.commit()
    key = c.lastrowid
    print(key)
    command = "INSERT INTO chapters (story_id, content, author, date) VALUES (?,?,?,?)"
    val = (key, first_chapter, author, date)
    c.execute(command, val)
    db.commit()

def returnStories():
    c.execute("SELECT story_name FROM stories")
    rows = c.fetchall()
    for row in rows:
        print(row)

def returnChapters():
    c.execute("SELECT content FROM chapters WHERE story_id =1")
    rows = c.fetchall()
    for row in rows:
        print(row)
    

def deleteStories():
    c.execute("DROP table stories")
    c.execute("DROP table chapters")

db.commit() #save changes
# c.execute("SELECT id, code FROM courses"):

# db.close()