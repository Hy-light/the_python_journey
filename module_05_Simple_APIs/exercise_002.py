import requests
import os

'''
Question 1: write  wget 

In the previous section, we used the wget function to retrieve content from the web server as shown below. Write the python code to perform the same task. The code should be the same as the one used to download the image, but the file name should be 'Example1.txt'.
!wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt
'''

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(),'example1.txt')
r = requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

'''
Get Request with URL Parameters

You can use the GET method to modify the results of your query, for example retrieving data from an API. We send a GET request to the server. Like before we have the Base URL, in the Route we append /get, this indicates we would like to preform a GET request.
The Base URL is for http://httpbin.org/ is a simple HTTP Request & Response Service. The URL in Python is given by:
'''

url_get = 'http://httpbin.org/get'

payload = {"name":"Joseph","ID":"123"}

r = requests.get(url_get, params=payload)
print(r.url)

print("request body:", r.request.body)

print(r.status_code)

print(r.text)

print(r.headers['Content-Type'])

print(r.json())

print(r.json()['args'])

'''
Post Requests

Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST
'''

url_post='http://httpbin.org/post'

'''
This endpoint will expect data as a file or as a form. A form is convenient way to configure an HTTP request to send data to a server.

To make a POST request we use the post() function, the variable payload is passed to the parameter  data :
'''

r_post = requests.post(url_post,data=payload)

print(r_post.url)

print("POST request body:", r_post.request.body)
print("GET request body:", r.request.body)

r_form = r_post.json()['form']
print(r_form)