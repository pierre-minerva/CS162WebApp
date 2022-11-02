from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('tasks', __name__)

@bp.route('/', methods=('GET', 'POST'))
@bp.route('/app', methods=('GET', 'POST'))
@bp.route('/home', methods=('GET', 'POST'))
@login_required
def app():
    db = get_db()
    if request.method == "POST":
        if request.form['operation'] == 'create':
            try:
                db.execute(
                    "INSERT INTO task (user_id, task_name, status) VALUES (?, ?, ?)",
                    (session.get('user_id'), request.form['task'], request.form['status']),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Task already exists."
            return render_template('tasks/app.html')
        elif request.form['operation'] == 'change':
            print(request.form['task'])
            try:
                db.execute(
                    "UPDATE task SET status=? WHERE user_id=? AND task_name=?",
                    (request.form['status'], session.get('user_id'), request.form['task']),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Task already exists."
            return render_template('tasks/app.html')
        else:
            try:
                db.execute(
                    "DELETE FROM task WHERE user_id=? AND task_name=?",
                    (session.get('user_id'), request.form['task']),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Task already exists."
            return render_template('tasks/app.html')
        
    else:
        task_lst = db.execute('SELECT task_name FROM task WHERE user_id={}'.format(session.get('user_id'))).fetchall()
        task_lst = [task[0] for task in task_lst]
        to_do_lst = db.execute('SELECT task_name FROM task WHERE user_id={} AND status="ToDo"'.format(session.get('user_id'))).fetchall()
        to_do_lst = [task[0] for task in to_do_lst]
        doing_lst = db.execute('SELECT task_name FROM task WHERE user_id={} AND status="Doing"'.format(session.get('user_id'))).fetchall()
        doing_lst = [task[0] for task in doing_lst]
        done_lst = db.execute('SELECT task_name FROM task WHERE user_id={} AND status="Done"'.format(session.get('user_id'))).fetchall()
        done_lst = [task[0] for task in done_lst]

        return render_template('tasks/app.html', task_lst=task_lst, to_do_lst=to_do_lst, doing_lst=doing_lst, done_lst=done_lst)