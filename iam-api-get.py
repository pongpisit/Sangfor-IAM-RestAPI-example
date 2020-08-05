import hashlib
import random
import requests

#################
iamIP='192.168.99.11'
iamPort='9999'
getStatement='/v1/user?name=ironman'

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

#####Make GET Request to IAM API###########
getMsg = ('http://'+iamIP+':'+iamPort+getStatement+'&random='+randomKey+'&md5='+md5)
print ('=====GET Request====')
print (getMsg)
r=requests.get(getMsg)
print ('=====Response====')
print (r.json())
