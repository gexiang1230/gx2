import requests
def listCourse():
  parma={'action': 'list_course','pagenum': '1','pagesize': 20}
  jsonstr=requests.get('http://localhost/api/mgr/sq_mgr/',params=parma)
  bodyDict=jsonstr.json()
  return [one['name'] for one in bodyDict["retlist"]]

if __name__ ==  "__main__" :
    cnamelist = listCourse()
    for one in cnamelist:
        print one
