#!/usr/bin/env python3

from flask import Flask, request

from controllers.home import homeController

app = Flask(__name__, static_url_path="/public", static_folder="/home/seif/projects/e-shop/seo-dashboard/public")

@app.get("/")
def index():
  return homeController(request)

if __name__ == "__main__":
  app.run(debug=True, port=8080, host="0.0.0.0")
