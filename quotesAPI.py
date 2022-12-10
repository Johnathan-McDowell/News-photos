import datetime
import requests

#Code adapted from code snippet section on https://rapidapi.com/saicoder/api/famous-quotes4. Modifications
#were made on the query string 
def quotes():
	url = "https://famous-quotes4.p.rapidapi.com/random"

	querystring = {"category":"motivational","count":"1"} 

	headers = {
		"X-RapidAPI-Key": "8fdc8b1cf0msh3cdcc3958d49bcbp11f9fbjsnad0b8d0faac1",
		"X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	return (response.json()[0]['text'])

def day_in_history():

	today = datetime.datetime.now()
	date = today.strftime('%m/%d')

	url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date

	headers = {
	'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzZDEyYzA1OTBjNmM1MTYyMWYxZTUyMDg1ZTE3M2UzNiIsImp0aSI6IjQ0YzkwNmVlMDk3ZDcxZTQyNTE1MzE3ODNiM2I4OTVkNzMzMDNlMDhhNzI3ZTEyODczNzFmYjdmYWRhN2ZlNzc2ZThmNThlNDdlZjlkZGJkIiwiaWF0IjoxNjcwNjMwMzU5LjI3MjU0OSwibmJmIjoxNjcwNjMwMzU5LjI3MjU1MiwiZXhwIjozMzIyNzUzOTE1OS4yNzAwNiwic3ViIjoiNzE0MDc4NTYiLCJpc3MiOiJodHRwczovL21ldGEud2lraW1lZGlhLm9yZyIsInJhdGVsaW1pdCI6eyJyZXF1ZXN0c19wZXJfdW5pdCI6NTAwMCwidW5pdCI6IkhPVVIifSwic2NvcGVzIjpbImJhc2ljIl19.pRLvh2XOWPfbEAHKE3ZhLQALxTpZju5vWTf25wj0fHISZIh6ATk2ZZK95a5bQeoYBxI5AKWeX2xuMW3-TqrtShWNnorcGzc6Xx-XJaIE7nKzFaG5YoNoUNvowYG4txunPK18djyty2tpGXioqZL7cVgc4eirunnhUbyCRFDnDLf3yaqqK_CA5ShXhcykXC5HGab8u4mhhJs6CjH6ikhjSupB4K8RriLkR6ujO9RtfiZyOUIxoYtuge7u5dhCqw9035bte7yswIHJHp7YpL8vGgIi6IO0K_eVvlxenuNqTOILso09kHOxHbsnI_xsr4DBa6alowrt4QU_L5qexcqeoYo68-HWzy0haf6o_P_dIgQA_ehC3kGm6jJlNCozOHryezSIsdyCElblMpQF0UYAeJKocX7o4RJnC1pKral0sX3LB1k1yYLtT8-5Z8WK8NwcvPfIspUh5hmVha6nqQM9jbBL8XMlcjQhmWwcqqvonq-wSrJpW1ZlRj-VQiHfRLF685bC38sdxcEyPnX_sa_uNarsjvuQfhSrdqmhoYFBb5VsUiXL-RhcU9Q8DblZVW1uCti1CRFxyhB5DgkUSTxu3jut6QSk9WVM5VZP9jQaKtOcxUqH-NvpeldHJ0anlaQqf4rk3TiUy9tq_78l5gFSC2Mi1WEtuUdDVJNNmojxUqU',
	'User-Agent': 'Week in photos'
	}

	response = requests.get(url, headers=headers)
	data = response.json()
	text = "Today in history!\n"+" in "+  str(data['events'][0]['year'])+ " " +data['events'][0]['text']	
	return text
