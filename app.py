# app.py
from flask import Flask, jsonify, request
from db import SessionLocal
from models import Counter

app = Flask(__name__)

@app.route('/get_counter', methods=['GET'])
def get_counter():
    db = SessionLocal()
    counter = db.query(Counter).first()
    if not counter:
        counter = Counter(value=0)
        db.add(counter)
        db.commit()
    db.close()
    return jsonify({'value': counter.value})

@app.route('/update_counter', methods=['POST'])
def update_counter():
    data = request.get_json()
    value = data.get('value')
    db = SessionLocal()
    counter = db.query(Counter).first()
    if not counter:
        counter = Counter(value=value)
        db.add(counter)
    else:
        counter.value = value
    db.commit()
    db.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)