from flask import Flask, render_template, request
import os, subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    for key in ['token', 'convo', 'file', 'hatersname', 'time', 'password']:
        file = request.files.get(key)
        if file:
            file.save(os.path.join(UPLOAD_FOLDER, key + '.txt'))
    try:
        output = subprocess.check_output(['python3', 'main.py'], stderr=subprocess.STDOUT, text=True)
        return "<pre>" + output + "</pre>"
    except subprocess.CalledProcessError as e:
        return "<b>❌ Error running script:</b><br><pre>" + e.output + "</pre>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
