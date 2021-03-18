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
##postStatement='/v1/user?_method=GET'
##pload={'random':randomKey,'md5':md5,
##       'search_type':'user',
##       'search_value':'spiderman'
##       }

### 2.Add Users ###
##postStatement='/v1/user'
##pload={'random':randomKey,'md5':md5,
##       'name': 'spiderman', #username
##       'desc': 'Added by RestAPI', #description
##       'father_path': '/guest', #group
##       'expire_time': expireDate, #expire date&time
##       'extend':{
##           'custom_cfg': { #additional user attribute
##               'Full Name': 'Peter Parker', 
##               'Sex': 'Male',
##               },
##           'self_pass': {
##               'enable': 'true', #enable local password
##               'password': '1234', #local password
##               'modify_once': 'false'
##               }
##           }
##       }

### 3. Edit Users ###
##postStatement='/v1/user?_method=PUT'
##pload={'random':randomKey,'md5':md5,
##    'name': 'hulk', #username
##    'data': {
##        'desc': 'Edited by RestfulAPI', #description
##        'expire_time': '2020-08-11 14:40', #expire date&time
##        'extend': {
##            'father_path': '/', #group
##            }
##        }
##    }


### 4. Put User to online SSO ###
postStatement='/v1/online-users'
pload={'random':randomKey,'md5':md5,
       "ip": "172.16.10.101",
       "name": "spiderman",
       "group": "/post",
       }
       
   

#####Make POST Request to IAM API###########
postMsg = ('http://'+iamIP+':'+iamPort+postStatement)
print ('=====POST Request====')
print (postMsg)
print ('=====POST Payload====')
print (pload)
r=requests.post(postMsg, json=pload)
print ('=====Response====')
print (r.json())
