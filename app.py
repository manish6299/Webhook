from flask import Flask, request, jsonify, render_template
from datetime import datetime
from config import collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    action_type = determine_action(data)

    if not action_type:
        return jsonify({'status': 'ignored'}), 400

    doc = {
        "request_id": get_request_id(data),
        "author": data['sender']['login'],
        "action": action_type,
        "from_branch": get_from_branch(data),
        "to_branch": get_to_branch(data),
        "timestamp": datetime.utcnow().isoformat()
    }

    collection.insert_one(doc)
    return jsonify({'status': 'success'}), 201

@app.route('/latest-events')
def latest_events():
    docs = collection.find().sort("timestamp", -1).limit(10)
    formatted = [format_event(doc) for doc in docs]
    return jsonify(formatted)

def get_request_id(data):
    if 'pull_request' in data:
        return str(data['pull_request']['id'])
    return data.get('after', 'unknown')

def get_from_branch(data):
    if 'pull_request' in data:
        return data['pull_request']['head']['ref']
    return data.get('ref', '').split('/')[-1]

def get_to_branch(data):
    if 'pull_request' in data:
        return data['pull_request']['base']['ref']
    return 'main'

def determine_action(data):
    if data.get('action') == 'opened':
        return 'PULL_REQUEST'
    if data.get('action') == 'closed' and data.get('pull_request', {}).get('merged'):
        return 'MERGE'
    if 'commits' in data:
        return 'PUSH'
    return None

def format_event(doc):
    dt = datetime.fromisoformat(doc['timestamp'])
    date_str = dt.strftime("%d %B %Y - %I:%M %p UTC")
    if doc['action'] == 'PUSH':
        return f'"{doc["author"]}" pushed to "{doc["to_branch"]}" on {date_str}'
    elif doc['action'] == 'PULL_REQUEST':
        return f'"{doc["author"]}" submitted a pull request from "{doc["from_branch"]}" to "{doc["to_branch"]}" on {date_str}'
    elif doc['action'] == 'MERGE':
        return f'"{doc["author"]}" merged branch "{doc["from_branch"]}" to "{doc["to_branch"]}" on {date_str}'
    return ''

if __name__ == '__main__':
    app.run(debug=True)
