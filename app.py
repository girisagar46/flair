import csv
import os

from flask import Flask
from flask import render_template

from services.ReportFetchService import fetch_files
from settings import DATA_STATIC

app = Flask(__name__)
static_dir = os.path


@app.route("/")
def index():
    with open(os.path.join(DATA_STATIC, "fyp.csv")) as file:
        dList = []
        reader = csv.DictReader(file)
        for row in reader:
            dList.append(row)
    return render_template("index.html", data=dList)


@app.route("/view/<roll>")
def view_content(roll):
    report_data = fetch_files(roll.split("&"))
    return render_template("details.html", data=report_data)


if __name__ == "__main__":
    app.run(debug=True)
