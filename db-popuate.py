import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "QuestionBank.db")

con=sqlite3.connect(db_path)
c=con.cursor()
c.execute('''
insert into QuestionsAnswersTable (Question, Answer_1, Answer_2,Answer_3) values
('What is the popular programing language?', 'Python', 'C', 'C+')
''')
con.commit()
con.close()