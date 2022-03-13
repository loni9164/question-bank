import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "QuestionBank.db")

con=sqlite3.connect(db_path)
c=con.cursor()
c.execute('''
create table QuestionsAnswersTable
(Question text,
Answer_1 text,
Answer_2 text,
Answer_3 text)
''')
con.commit()
con.close()
