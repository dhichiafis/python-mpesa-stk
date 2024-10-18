import requests 
import json
from requests.auth import HTTPBasicAuth
rl='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
#response=requests.get(url,headers = { 'Authorization': 'Basic TWtHR3NvMDNJdm5aR0dPUmwwQ25ERWMyMHZ0bFlySlNZWnFIRXZsWmFwYkczQVB0OjduM0ZiOW90WTRkR3R6MkNheVptWWJHWjBhTVFjQ1lBTkdjRkFseUFuT1RrYkFtbXZWSGlVdTZMZTdLTGFrQ28='})
url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
consumer_key='MkGGso03IvnZGGORl0CnDEc20vtlYrJSYZqHEvlZapbG3APt'
consumer_secret='7n3Fb9otY4dGtz2CayZmYbGZ0aMQcCYANGcFAlyAnOTkbAmmvVHiUu6Le7KLakCo'
response=requests.get(url=url,auth=HTTPBasicAuth(consumer_key,consumer_secret))
#print(r.headers)

print(response.text)
access_token=response.json()['access_token']
print(access_token)
new_url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
formData={    
   "BusinessShortCode": "174379",    
   "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",    
   "Timestamp":"20160216165627",    
   "TransactionType": "CustomerPayBillOnline",    
   "Amount": "1",    
   "PartyA":"254715921815",    
   "PartyB":"174379",    
   "PhoneNumber":"254715921815",    
   "CallBackURL": "https://mydomain.com/pat",    
   "AccountReference":"Test",    
   "TransactionDesc":"Test"
}


new_r=requests.post(new_url,data=json.dumps(formData),headers=headers)
print(new_r.text)
print(new_r.status_code)
