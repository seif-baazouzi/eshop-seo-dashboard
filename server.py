#!/usr/bin/env python3

from datetime import date
from flask import Flask, render_template

from db.mongo import db

app = Flask(__name__, static_url_path="/public", static_folder="/home/seif/projects/e-shop/seo-dashboard/public")

@app.get("/")
def index():
  today = date.today().strftime("%Y-%m-%d")
  log = db.logs.find_one({ "date": today })

  return render_template("index.html", log=log, fields=[ "users", "shops", "items", "carts", "shopsRates", "itemsRates" ])

if __name__ == "__main__":
  app.run(debug=True, port=8080, host="0.0.0.0")
