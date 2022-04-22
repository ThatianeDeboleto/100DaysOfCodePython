from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, timedelta
import random, string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'

db = SQLAlchemy(app)


class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now().date)


def __repr__(self):
    return date_created


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_datetime')
def send_datetime():
    date_time = datetime.now().date()
    x = ''.join(random.choice(string.digits) for _ in range(16))
    try:
        new_log = Logs(id=int(x), date_created=date_time)
    except:
        x = ''.join(random.choice(string.digits) for _ in range(16))
        new_log = Logs(id=int(x), date_created=date_time)
    db.session.add(new_log)
    db.session.commit()
    return redirect('/')


def calculate_today():
    logs = Logs.query.order_by(Logs.date_created).all()
    count = 0
    for i in logs:
        if i.date_created.date() == datetime.now().date():
            count += 1
    return count


def calculate_yesterday():
    logs = Logs.query.order_by(Logs.date_created).all()
    count = 0
    for i in logs:
        if i.date_created.date() == datetime.now().date() - timedelta(days=1):
            count += 1
    return count


def calculate_7_days():
    logs = Logs.query.order_by(Logs.date_created).all()
    count = 0
    for i in logs:
        if i.date_created.date() >= datetime.now().date() - timedelta(days=7):
            count += 1
    return float(count / 7)


def calculate_30_days():
    logs = Logs.query.order_by(Logs.date_created).all()
    count = 0
    for i in logs:
        if i.date_created.date() >= datetime.now().date() - timedelta(days=30):
            count += 1
    return float(count / 30)


@app.route('/history')
def history():
    data = {
        'today': calculate_today(),
        'yesterday': calculate_yesterday(),
        'seven_days': round(calculate_7_days(), 2),
        'thirty_days': round(calculate_30_days(), 2)
    }
    return render_template('history.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)

