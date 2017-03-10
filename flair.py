from flask import Flask
from flask import render_template

from settings import APP_STATIC, DATA_STATIC
import csv, os

app = Flask(__name__)
static_dir = os.path

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/')
def index():
    with open(os.path.join(DATA_STATIC, 'fyp.csv'), 'rb') as file:
        dList = []
        reader = csv.DictReader(file)
        for row in reader:
            dList.append(row)
    return render_template("index.html", data = dList)

if __name__ == '__main__':
    app.run(debug=True)
