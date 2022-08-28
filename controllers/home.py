from datetime import datetime
from flask import render_template

from models.logs import getLastLog, getMonthLogs
from utils.formatLogs import formatLogs

def homeController(request):
  queryParams = request.args.to_dict()  
  if "month" in queryParams:
    month = queryParams["month"]
  else:
    today = datetime.now()
    month = f"{today.year}-{str(today.month).rjust(2, '0')}"

  log = getLastLog()
  logs = getMonthLogs(month)

  return render_template(
    "index.html",
    log=log,
    month=month,
    options=formatLogs(logs),
    fields=[ "users", "shops", "items", "carts", "shopsRates", "itemsRates" ]
  )
