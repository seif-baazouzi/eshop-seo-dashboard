import json

def formatLogs(logs):
  if len(logs) == 0:
    return "{}"
  
  data = {}
  labels = []
  fields = [ "users", "shops", "items", "carts", "shopsRates", "itemsRates" ]

  for log in logs:
    labels.append(log["date"])
    for field in fields:
      if field not in data:
        data[field] = []   
      data[field].append(log[field])

  return json.dumps({
    "xAxis": {
      "data": labels
    },
    "tooltip": {
      "trigger": "axis"
    },
    "legend": {
      "data": fields,
      "top": "bottom"
    },
    "yAxis": {},
    "series": [ ({ "name": field, "data": data[field], "type": "line", "stack": "x" }) for field in fields ]
  })
