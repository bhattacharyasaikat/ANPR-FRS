import requests

url = "https://sms77io.p.rapidapi.com/sms"

payload = "to=%2B491771783130&p=%3CREQUIRED%3E&text=Dear%20customer.%20We%20want%20to%20say%20thanks%20for%20your%20trust.%20Use%20code%20MINUS10%20for%2010%20%25%20discount%20on%20your%20next%20order!"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "QxEtwstydBzbrBQ35EC8irjaZDVCaYJm8KSITwUs5ORhHlgw5hrGY7iKhW14qnov",
	"X-RapidAPI-Host": "sms77io.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)