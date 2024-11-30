from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/execute')
def execute_js():
    # Execute JavaScript using Node.js subprocess
    import subprocess
    result = subprocess.run(['node', 'static/script.js'], capture_output=True, text=True)
    return jsonify({'result': result.stdout})