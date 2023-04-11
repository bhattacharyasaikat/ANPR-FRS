import requests
import datetime

url = "https://vehicle-rc-information.p.rapidapi.com/"

payload = {"VehicleNumber": "WB20AX4245"}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "0c067474f7mshe0515c9344a4e36p1afde5jsn13ab9170907d",
	"X-RapidAPI-Host": "vehicle-rc-information.p.rapidapi.com"
}

def check_validity(response, field): # define a function that takes a response object and a field name as arguments
  response_dict = response.json() # convert response text to dictionary
  valid_upto = response_dict["result"][field] # get valid_upto value for the given field
  valid_date = datetime.datetime.strptime(valid_upto, "%Y-%m-%d") # convert valid_upto string to datetime object
  today = datetime.datetime.now() # get current date and time
  if valid_date > today: # compare valid_date with today
    return True # return True if valid_date is later than today
  else:
    return False # return False if valid_date is earlier than or equal to today

response = requests.request("POST", url, json=payload, headers=headers)

#print(response.text)
response_dict = response.json() # convert response text to dictionary
owner_name = response_dict["result"]["owner_name"] # get owner name
fuel_type = response_dict["result"]["fuel_type"] # get fuel type
seat = response_dict["result"]["seating_capacity"]

#request
fitness_validity = check_validity(response, "fitness_upto") # fitness_upto field and assign the result to a variable
insurance_validity = check_validity(response, "insurance_validity") # insurance_validity field and assign the result to a variable
puc_validity = check_validity(response, "puc_valid_upto") #  puc_valid_upto field and assign the result to a variable
print("Car Validation: ",fitness_validity) 
print("Insurance Validation: ",insurance_validity) 
print("pollution status:",puc_validity) 

#check if its neccassary to print these.
print("Car Owner Name: ",owner_name) 
print("Fuel type: ",fuel_type) 
print("Seat capacity: ",seat)
