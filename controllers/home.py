from flask import render_template

from models.logs import getLastLog

def homeController():
  log = getLastLog()

  return render_template(
    "index.html",
    log=log,
    fields=[ "users", "shops", "items", "carts", "shopsRates", "itemsRates" ]
  )
