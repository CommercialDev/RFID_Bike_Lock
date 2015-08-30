import requests
token = "hjFCXDfKWCfiBbpIhvaasdfjbbDrSW31"
head = {'X-ZUMO-APPLICATION': "hjFCXDfKWCfiBbpIhvaasdfjbbDrSW31"}
url = "https://trailmonitorservice.azure-mobile.net/api/verifyEmployee?empId=<employeeID>"
r = requests.get(url, headers=head)
print(r)
