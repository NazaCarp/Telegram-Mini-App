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


@app.route('/boosts.html')
def serve_boosts():
    return render_template('boosts.html')


@app.route('/get_counters', methods=['GET'])
def get_counters():
    user_id = request.args.get('user_id')
    startParam = request.args.get('startParam')
    name = request.args.get('name')
    username = request.args.get('username')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            counter = Counter(user_id=user_id, name=name, username=username, score=0, secondarycount=0, tap=1, energy_limit=1000, recharge_speed=1)
            db.add(counter)
            db.commit()

            # Crear la tabla referrals para el nuevo usuario
            referral = Referral(user_id=user_id, name=name, from_user=startParam, referrals_count=0, referrals_name='', referrals_id=None)
            db.add(referral)
            db.commit()
        
            # Incrementar el número de referidos
            if startParam.isdigit():
                referrer = db.query(Referral).filter_by(user_id=startParam).first()
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

                referrer_counter = db.query(Counter).filter_by(user_id=int(startParam)).first()
                referrer_counter.score += 100
                db.commit()

        return jsonify({
            'score': counter.score,
            'secondarycount': counter.secondarycount,
            'timestamp': counter.timestamp.replace(tzinfo=timezone.utc).isoformat(),  # Convertir a ISO 8601 con UTC
            'tap': counter.tap,
            'energy_limit': counter.energy_limit,
            'recharge_speed': counter.recharge_speed
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


@app.route('/get_referrals', methods=['GET'])
def get_referrals():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        referral = db.query(Referral).filter_by(user_id=user_id).first()
        if not referral:
            return jsonify({'referrals_count': 0, 'referrals_name': '', 'referrals_score': '', 'referrals_username': ''})

        referrals_id = referral.referrals_id.split(', ') if referral.referrals_id else []
        referrals_name = referral.referrals_name.split(', ') if referral.referrals_name else []
        referrals_score = []
        referrals_username = []

        for ref_id in referrals_id:
            counter = db.query(Counter).filter_by(user_id=int(ref_id)).first()
            if counter:
                referrals_score.append(str(counter.score))
                referrals_username.append(str(counter.username))
            else:
                referrals_score.append('0')
                referrals_username.append('0')

        return jsonify({
            'referrals_count': referral.referrals_count,
            'referrals_name': ', '.join(referrals_name),
            'referrals_score': ', '.join(referrals_score),
            'referrals_username': ', '.join(referrals_username)
        })
    except Exception as e:
        logging.error(f"Error in get_referrals: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'score': counter.score,
            'tap': counter.tap,
            'energy_limit': counter.energy_limit,
            'recharge_speed': counter.recharge_speed
        })
    except Exception as e:
        logging.error(f"Error in get_user_data: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/update_boost', methods=['POST'])
def update_boost():
    data = request.get_json()
    user_id = data.get('user_id')
    score = data.get('score')
    boost_type = data.get('boost_type')
    cost = data.get('cost')

    if not all([user_id, score, boost_type, cost]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        db = SessionLocal()
        counter = db.query(Counter).filter_by(user_id=user_id).first()
        if not counter:
            return jsonify({'error': 'User not found'}), 404

        counter.score = score
        if boost_type == 'multitap':
            counter.tap += 1
        elif boost_type == 'energy_limit':
            counter.energy_limit = (counter.energy_limit or 1000) + 500
        elif boost_type == 'recharge_speed':
            counter.recharge_speed = (counter.recharge_speed or 1) + 1

        db.commit()
        return jsonify({'status': 'success'})
    
    except Exception as e:
        logging.error(f"Error in update_boost: {e}")
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)