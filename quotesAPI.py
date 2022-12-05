import requests
import json 

#Code adapted from code snippet section on https://rapidapi.com/saicoder/api/famous-quotes4. Modifications
#were made on the query string 

url = "https://famous-quotes4.p.rapidapi.com/random"

querystring = {"category":"motivational","count":"1"} 

headers = {
	"X-RapidAPI-Key": "8fdc8b1cf0msh3cdcc3958d49bcbp11f9fbjsnad0b8d0faac1",
	"X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
