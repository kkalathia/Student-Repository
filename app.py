from flask import Flask, render_template
import sqlite3
from typing import Dict

DB_FILE: str = "Open path" """(810_Assignments.db)"""

app = Flask(__name__)


@app.route('/Hello/')
def hello_world():
    return 'Hello World! This is Flask'


@app.route('/Goodbye/')
def see_ya():
    return 'See You Later!!'


@app.route('/student_summary/')
def student_summary() -> str:
    query = "select s.name, s.cwid, g.Course, g.Grade,i.name from students s join grades as g on s.cwid = " \
            "g.StudentCWID join instructors i on i.cwid = g.InstructorCWID order by s.name ASC "

    db: sqlite3.Connection = sqlite3.connect(DB_FILE)

    data: Dict[str, str] = [{
        'name': name, 'cwid': cwid, 'course': course, 'grade': grade, 'instructor': instructor}
        for cwid, name, course, grade, instructor in db.execute(query)
    ]

    db.close()
    return render_template('student.html', title="Steves Repository", table_title=" Stevens Institute of Technology",
                           students=data)


if __name__ == '__main__':
    app.run(debug=True)
