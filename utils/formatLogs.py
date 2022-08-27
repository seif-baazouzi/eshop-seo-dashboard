import json

def formatLogs(logs):
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
    "yAxis": {},
    "series": [ ({ "data": data[field], "type": "line", "stack": "x" }) for field in fields ]
  })
