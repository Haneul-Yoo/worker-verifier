import os
import random
from flask import Flask, redirect, request, render_template

app = Flask(__name__)
output_path = '.'

def is_user_id(uid):
    file_path = '%s/user_ids/%s.json' % (output_path, uid)
    return os.path.exists(file_path)

def generate_user_id(wid):
    while True:
        uid = ''.join(random.choice('abcedfghijklmnopqrstuvwxyz0123456789') for i in range(16))
        if not is_user_id(uid):
            break
    file_path = '%s/user_ids/%s.json' % (output_path, uid)
    with open(file_path, 'w') as f:
        f.write(wid)
    return uid

@app.route('/')
@app.route('/verify')
@app.route('/verify/')
def task_index():
    return render_template('verifier.html')

@app.route('/done')
@app.route('/done/')
def task_done():
    args_dict = request.args.to_dict()
    wid = args_dict['wid']
    code = generate_user_id(wid)
    return render_template('done.html', code=code)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)