import hashlib
import random
import requests
from datetime import datetime


###Initial Variables###
iamIP='192.168.99.11'
iamPort='9999'
expireIn = 5 #days
expireDate= str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day+expireIn)+' 00:00:00'

### Generate Random Key ####
iamKey='123'
randomKey=str(random.randrange(9999))
combineKey = iamKey+randomKey
md5 = hashlib.md5(combineKey.encode('utf-8')).hexdigest()

### Print Generated Key ###
print ('=====Key Indicator====')
print ('Presharekey='+iamKey)
print ('Random='+randomKey)
print ('Hash='+md5)

### POST Function ###

### 1.Search Users ###
postStatement='/v1/user?_method=GET'
pload={'random':randomKey,'md5':md5,
       'search_type':'user',
       'search_value':'spider'
       }

### 2.Add Users ###
postStatement='/v1/user'
pload={'random':randomKey,'md5':md5,
       'name': 'black_widow',
       'desc': 'Added by RestAPI',
       'father_path': '/guest-selfregister',
       'expire_time': expireDate,
       'extend':{
           'custom_cfg': {
               'Full Name': 'Natasha Romanoff', 
               'Sex': 'Female',
               'Team': 'Avengers'
               },
           'self_pass': {
               'enable': 'true',
               'password': '1234',
               'modify_once': 'false'
               }
           }
       }

### 3. Edit Users ###
##postStatement='/v1/user?_method=PUT'
##pload={'random':randomKey,'md5':md5,
##    'name': 'hulk',
##    'data': {
##        'desc': 'Edited by RestfulAPI',
##        'expire_time': '2021-01-10 00:00:00',
##        'extend': {
##            'father_path': '/avenger',
##            }
##        }
##    }
   
#####Make POST Request to IAM API###########
postMsg = ('http://'+iamIP+':'+iamPort+postStatement)
print ('=====POST Request====')
print (postMsg)
print ('=====POST Payload====')
print (pload)
r=requests.post(postMsg, json=pload)
print ('=====Response====')
print (r.json())
