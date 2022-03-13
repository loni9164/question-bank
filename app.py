from flask import Flask, render_template, request
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "QuestionBank.db")

app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        Question = request.form['Question']
        con = sqlite3.connect(db_path)
        c = con.cursor()
        result=c.execute(f"select * from QuestionsAnswersTable where Question='{Question}';")
        try:
            result=result.fetchall()[0]
            return render_template('SearchResult.html', result=result)
        except:
            result2=[Question,'NA','NA','NA']
            c.execute("insert into QuestionsAnswersTable (Question,Answer_1,Answer_2,Answer_3) values (?,?,?,?)",(result2))
            con.commit()
            return render_template('SearchResult.html',result=result2)
        con.close()

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'GET':
        return render_template('update.html')
    else:
        Question = request.form['Question']
        Answer_1 = request.form['Answer_1']
        Answer_2 = request.form['Answer_2']
        Answer_3 = request.form['Answer_3']
        con=sqlite3.connect(db_path)
        c=con.cursor()
        c.execute('''update QuestionsAnswersTable SET Answer_1=:Answer_1, Answer_2=:Answer_2,
         Answer_3=:Answer_2 where Question = :Question''',
                  {'Answer_1': Answer_1, 'Answer_2': Answer_2, 'Answer_3': Answer_3, 'Question': Question})
        con.commit()
        result = c.execute(f"select * from QuestionsAnswersTable where Question='{Question}';")
        try:
            result=result.fetchall()[0]
            return render_template('DataBaseUpdated.html')
        except:
            return render_template('NoRecordExist.html')
        con.close()

if __name__=='__main__':
    app.run(debug=True)