from flask import Flask, jsonify, request, render_template
from db import SessionLocal
from models import Counter
import logging

app = Flask(__name__, template_folder='.')

# Configurar logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_counter', methods=['GET'])
def get_counter():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, value=0)
            db.add(counter)
            db.commit()
        db.close()
        return jsonify({'value': counter.value})
    except Exception as e:
        logging.error(f"Error in get_counter: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/update_counter', methods=['POST'])
def update_counter():
    data = request.get_json()
    user_id = data.get('user_id')
    value = data.get('value')

    if not user_id or value is None:
        return jsonify({'error': 'user_id and value are required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, value=value)
            db.add(counter)
        else:
            counter.value = value
        db.commit()
        db.close()
        return jsonify({'status': 'success'})
    except Exception as e:
        logging.error(f"Error in update_counter: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)