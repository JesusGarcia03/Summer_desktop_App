import requests

Test_url = "https:/httpbin.org"

#response = requests.get(TEST_url + '/get')
#response = response.json()

#response = requests.get(TEST_url + '/get' headers={'user-A'})
response = requests.get(TEST_url+'get?test=hellp&other=world', headers = {'User-Agent':'Its me mario'})
code = print(response)
response = response.json()
print(response)