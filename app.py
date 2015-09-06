import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
	return render_template("index.html")

@app.route("/scheduler")
def scheduler():
	return render_template("scheduler.html")

@app.route("/restrictions")
def restrictions():
	return render_template("restrictions.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)