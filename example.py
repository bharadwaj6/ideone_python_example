# Read comments to understand what the following snippet does.

# these are used in almost every API call we make to ideone.
# API password is different from Account password. 
# Checkout ideone settings for your account to setup one.
USER = "username"
PASS = "password"

###########################################################

# not ideone related, but to test your SOAPpy installation.

# clients.py
import SOAPpy
local_client = SOAPpy.SOAPProxy("http://localhost:8080/")
print local_client.hello()

# server.py
from SOAPpy import SOAP
def hello():
	return "Hello World! SOAP server here!"

local_server = SOAP.SOAPServer(("localhost", 8080))
s=local_server.registerFunction(hello)
local_server.serve_forever()

# Creating WSDLObject => First step.
from SOAPpy import WSDL
wsdlObject = WSDL.Proxy("http://ideone.com/api/1/service.wsdl")

###########################################################

# A trivial getLanguages() call.
wsdlObject.getLanguages(USER, PASS)

# A formatted version of what get_languages() returns. 
# Use this for easier control over languages.
languages = wsdlObject.getLanguages(USER, PASS)
result_dict = {}
property_list = languages.item
for item in property_list:
	result_dict[item.key[0]] = item.value[0]
languages_list = result_dict.items()[1][1]
simple_languages = dict((k,v.split('(')[0].strip()) for (k,v) in languages_list)

# you can use languages_list and simple_languages to get 
# id of a language, if their name is given.
# Example: To get id of python. By default, it gives me id of Python 2.7.
LANGUAGE_NAME = "Python"
def get_language_id(LANGUAGE_NAME):
	for index, name in simple_languages.items():
		if name.lower() == LANGUAGE_NAME.lower():
			return index

###########################################################

