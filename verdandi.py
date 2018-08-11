from db import get_db, close_db

from flask import Flask, request, jsonify, abort


app = Flask(__name__)
app.config['DATABASE'] = 'database'

@app.route("/")
def hello():
    return "Hello World!"


def add_events_to_schedule(schedule):
    db = get_db()
    db_result = db.execute(
            'SELECT id FROM events WHERE schedule_id = ?',
            (schedule['id'],)
        )
    schedule['event_ids'] = [event['id'] for event in db_result]


@app.route('/schedules/', methods=['GET', 'POST'])
def manage_schedules():
    if request.method == 'GET':
        return get_schedules()
    elif request.method == 'POST':
        return post_schedule()


def get_schedules():
    db = get_db()
    db_result = db.execute('SELECT * FROM schedules')
    schedules = [dict(schedule) for schedule in db_result]
    for schedule in schedules:
        add_events_to_schedule(schedule)
    close_db()
    return jsonify(schedules)


def post_schedule():
    name = request.get_json(force=True)['name']
    db = get_db()
    schedules = db.execute('INSERT INTO schedules(name) VALUES(?)',(name,))
    db.commit()
    close_db()
    return 'Schedule with name ' + name + ' created'


@app.route('/schedules/<int:schedule_id>', methods=['GET'])
def manage_schedule(schedule_id):
    db = get_db()
    db_result = db.execute(
        'SELECT * FROM schedules WHERE id = ?',
        (schedule_id,)
    ).fetchone()

    if db_result == None:
        abort(404)

    schedule = dict(db_result)
    add_events_to_schedule(schedule)
    return jsonify(schedule)


@app.route('/events/', methods=['GET', 'POST'])
def manage_events():
    if request.method == 'GET':
        return get_events()
    elif request.method == 'POST':
        return post_event()


def get_events():
    db = get_db()
    db_result = db.execute('SELECT * FROM events')
    events = [dict(event) for event in db_result]
    close_db()
    return jsonify(events)


def post_event():
    request_data = request.get_json(force=True)

    name = request_data['name']
    schedule = request_data['schedule']

    db = get_db()
    events = db.execute(
        'INSERT INTO events(schedule_id, name) VALUES(?,?)',
        (schedule,
         name)
    )
    db.commit()
    close_db()

    return 'Event with name ' + name + ' created'


@app.route('/events/<int:event_id>', methods=['GET'])
def manage_event(event_id):
    db = get_db()
    db_result = db.execute(
        'SELECT * FROM events WHERE id = ?',
        (event_id,)
    )
    event = db_result.fetchone()

    if event == None:
        abort(404)

    close_db()
    return jsonify(dict(event))
