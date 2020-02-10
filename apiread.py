import requests

url = 'https://reqres.in/api/users'
resp = requests.get(url)
resp.raise_for_status()
apiData = resp.json()
emlList = [email['email'] for email in apiData['data']]
for email in emlList:
	print(email)