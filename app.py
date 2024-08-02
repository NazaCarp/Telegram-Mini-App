from datetime import datetime, timezone
from flask import Flask, jsonify, request, render_template
from db import SessionLocal
from models import Counter, Referral
import logging

app = Flask(__name__, template_folder='.')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/friends.html')
def serve_friends():
    return render_template('friends.html')

@app.route('/get_counters', methods=['GET'])
def get_counters():
    user_id = request.args.get('user_id')
    start_param = request.args.get('startParam')
    name = request.args.get('name')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        user_id = int(user_id)  # Convertir a int si es necesario
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, name=name, score=0, secondarycount=0, tap=1)
            db.add(counter)
            db.commit()

            # Crear la tabla referrals para el nuevo usuario
            referral = Referral(user_id=user_id, name=name, from_user=start_param, referrals_count=0, referrals_name='', referrals_id=None)
            db.add(referral)
            db.commit()
        
        # Incrementar referralscount para el user_id igual a start_param
        if start_param.isdigit():
            referrer = db.query(Referral).filter_by(user_id=int(start_param)).first()
            if referrer:
                referrer.referrals_count += 1
                if referrer.referrals_name:
                    referrer.referrals_name += f', {name}'
                else:
                    referrer.referrals_name = name
                if referrer.referrals_id:
                    referrer.referrals_id += f', {user_id}'
                else:
                    referrer.referrals_id = user_id
                db.commit()

                referrer_counter = db.query(Counter).filter_by(user_id=int(start_param)).first()
                referrer_counter.score += 100
                db.commit()

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