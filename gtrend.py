import requests

r=requests.get('http://hawttrends.appspot.com/api/terms/')
res=r.json()
res['3']
for i in res['3']:
    print('------------')
    print(i)