#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def index():
  return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
  app.run(debug=True, port=8080, host="0.0.0.0")
