import requests
import json
import time

from reqres.verification import Verify

class Apis():

    def getUnsub(self, url, apiKey, email):
        resp = requests.get(
            url+'/email/unsubscribes?api_key='+apiKey+'&email='+email)
        if resp.status_code == 200:
            return resp.json()
        else:
            print('Wrong request., check again')

    def postEmailStatus(self, url, apiKey, email, state):
        resp = requests.post(
            url+'/email/status?api_key='+apiKey+'&email='+email+'&subscription_state='+state)
        if resp.status_code == 201:
            return resp.json()
        else:
            print('Wrong request., check again')
    
    def cusEveLis(self, url, apiKey):
        resp = requests.get(url+'/events/list?api_key='+apiKey)
        # value = Verify.userProfileVerify()
        if resp.status_code == 200:
            return resp.json()
        else:
            print('Wrong request., check again')

    def cusEveAnal(self, url, apiKey, event, length, unit):
        print(url+'/events/data_series?&event='+event +'&length='+str(length) +'&unit='+unit+'&api_key='+apiKey)
        headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ****************************'
        }
        resp = requests.get(url+'/events/data_series?&event='+event +'&length='+str(length) +'&unit='+unit+'&api_key='+apiKey,headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            print('Wrong request., check again')
    
    def userpro(self,url,apiKey,ID):
        payload = json.dumps({
            "external_ids": ["Dafay","Gfddv","fyyfu"]     
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 	*******************************'
        }
        resp = requests.post(url+'/users/export/ids',data=payload,headers=headers)
        time.sleep(2)
        resp= Verify.userProfileVerify(resp.json())
        return resp



