from datetime import datetime, timezone
from flask import Flask, jsonify, request, send_from_directory, render_template
from db import SessionLocal
from models import Counter
import logging

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/index.html')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/friends.html')
def serve_friends():
    return render_template('.', 'friends.html')

@app.route('/get_counters', methods=['GET'])
def get_counters():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        user_id = int(user_id)  # Convertir a int si es necesario
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, score=0, secondarycount=0, tap=1)
            db.add(counter)
            db.commit()
        logging.info(f"Contadores obtenidos para user_id {user_id}: score={counter.score}, secondarycount={counter.secondarycount}, timestamp={counter.timestamp}, tap={counter.tap}")
        return jsonify({
            'score': counter.score,
            'secondarycount': counter.secondarycount,
            'timestamp': counter.timestamp.replace(tzinfo=timezone.utc).isoformat(),  # Convertir a ISO 8601 con UTC
            'tap': counter.tap
        })
    except Exception as e:
        logging.error(f"Error in get_counters: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/update_counters', methods=['POST'])
def update_counters():
    data = request.get_json()
    user_id = data.get('user_id')
    score = data.get('score')
    secondarycount = data.get('secondarycount')

    if not user_id or score is None or secondarycount is None:
        return jsonify({'error': 'user_id, score, and secondarycount are required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, score=score, secondarycount=secondarycount, timestamp=datetime.utcnow())
            db.add(counter)
        else:
            counter.score = score
            counter.secondarycount = secondarycount
            counter.timestamp = datetime.utcnow()
        db.commit()
        return jsonify({'status': 'success'})
    except Exception as e:
        logging.error(f"Error in update_counters: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)