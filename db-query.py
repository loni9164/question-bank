import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "QuestionBank.db")
con=sqlite3.connect(db_path)
c=con.cursor()

#c.execute('delete from QuestionsAnswersTable')
#con.commit()
#con.close()
result=c.execute('select * from QuestionsAnswersTable')
print(result.fetchall())

#reference
#result =c.execute(f"select * from QuestionsAnswersTable where Question='{Question}';")
#c.execute('''INSERT INTO QuestionsAnswersTable (Question,Answer_1,Answer_2,Answer_3) values ('Prashant','10','20','50')''')
#select Question from QuestionsAnswersTable where Question = 'What is the popular programing language?'
#INSERT INTO QuestionsAnswersTable (Question ) values (10)
#'select * from QuestionsAnswersTable'
#'select Question from QuestionsAnswersTable where Question=Question'
#'''INSERT INTO QuestionsAnswersTable (Question,Answer_1,Answer_2,Answer_3) values ('Prashant','10','20','50')'''
#print(result.fetchall())