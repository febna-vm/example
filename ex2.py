import json 
data={}
data={'site': 'vp_ind.com',
  'async': 'true',
  'sra': 'true',
  'networkId': '3081',
  'mobileSite': 'vp.m',
  'disableInitialLoad':'false',
  'zone': 'index'}
#print(data)

data1= {
    'nk': 'print',
    'pr': 'vp',
    'imp': 'index',
    'ck': 'index'
  }
data["keys"]=data1
#print(data)

data3={
      'name': 'gpt-impulse',
      'type': 'impulse'
    }

data4={
      "name": "gpt-wallpaper",
      "type": "wallpaper"
    }
l=[]
l.append(data3)
l.append(data4)
data["adslots"]=l


#print(data)
jsonfile=json.dumps(data)
print(jsonfile)