import requests
import json

class Verify():

    def userProfileVerify(resp):


        final_out= []

        for i in range(0,len(resp['users'])):
            output= {}
            output["external_id"]=resp["users"][i]["external_id"]
            

            try:
                output["custom_attributes"]=resp["users"][i]["custom_attributes"]
                output["user_aliases"]=resp["users"][i]["user_aliases"]
                output["first_name"]=resp["users"][i]["first_name"]
                output["last_name"]=resp["users"][i]["last_name"]
                output["email"]=resp["users"][i]["email"]
                output["custom_events"]=resp["users"][i]["custom_events"][0]['name']
                output["purchases_1"]=resp["users"][i]["purchases"][0]['name']
                output["purchases_count_1"]=resp["users"][i]["purchases"][0]['count']
                output["purchases_2"]=resp["users"][i]["purchases"][1]['name']
                output["purchases_count_2"]=resp["users"][i]["purchases"][1]['count']
                output["dob"]=resp["users"][i]["dob"]
                output["devices_idfv"]=resp["users"][i]["devices"][0]['idfv']
                output["devices_idfa"]=resp["users"][i]["devices"][0]['idfa']
                
            except KeyError:
                pass
            
            output["email_subscribe"]=resp["users"][i]["email_subscribe"]
            output["devices_model"]=resp["users"][i]["devices"][0]['model']
            output["devices_os"]=resp["users"][i]["devices"][0]['os']
            output["message"]=resp["message"]
            final_out.append(output)
        y = json.dumps(final_out)
        z = json.loads(y)
        return z


       
