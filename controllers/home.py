from flask import render_template

from models.logs import getLastLog, getMonthLogs
from utils.formatLogs import formatLogs

def homeController():
  log = getLastLog()
  logs = getMonthLogs()

  return render_template(
    "index.html",
    log=log,
    options=formatLogs(logs),
    fields=[ "users", "shops", "items", "carts", "shopsRates", "itemsRates" ]
  )
