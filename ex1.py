import json

data={}
data['key'] = []
data['key'].append({
  "site": "vp_ind.com",
  "async": true,
  "sra": true,
  "networkId": "3081",
  "mobileSite": "vp.m",
  "disableInitialLoad": false,
  "zone": "index"
})
json_data = json.dumps(data)
