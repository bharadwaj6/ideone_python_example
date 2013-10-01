# Read comments to understand what the following snippet does.
# You're free to use these snippets however you like. 
#
# Last tested on 1st October 2013.
#
# API password is different from Account password. 
# Checkout ideone settings for your account to setup one.
# They're used in every ideone API call.
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

###########################################################

# Creating WSDLObject => First step.
from SOAPpy import WSDL
wsdlObject = WSDL.Proxy("http://ideone.com/api/1/service.wsdl")

# test function to test your connection/ USER-PASS combination.
wsdlObject.testFunction(USER, PASS)

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

# A submission example. Submitting a file as my sourceCode.
# We could have also used a sample string like this instead:
# str1 = "print 'Hello World'"

f = open('hello.py', 'r')
str1 = f.read()
f.close()

# initializing all the arguments to be passed. Change them like you want.
sourceCode = str1
language = get_language_id('Python') # could have used the id too.
input = ""
run = True
private = True

# We need this object for accessing the link of this submission, which will be used for fetching results.
submission_object = wsdlObject.createSubmission(USER, PASS, sourceCode, language, input, run, private)

link = list(submission_object)[0][1]['value']

# To get status of the submission.
submission_status = wsdlObject.getSubmissionStatus(USER, PASS, link)

###########################################################

# choose your own values here.
withSource = True
withInput = True
withOutput = True
withStderr = True
withCmpinfo = True

# To get details of the submission.
submission_details = wsdlObject.getSubmissionDetails(USER, PASS, link, withSource, withInput, withOutput, withStderr, withCmpinfo)

# this is how you would read each detail of the submission, similar to one we did before.
#
# Convert the details result into something more approachable, because 
# this one could contain many key, value pairs depending on the parameters we might have passed. 
submission_details_list = list(submission_details)[0]
submission_details_dict = {}
for i in range(0, len(submission_details_list)):
	submission_details_dict[submission_details_list[i]['key']] = submission_details_list[i]['value']

# To access one of the values in the big details object created...
# for example result of the submission - you now have to just do this:
submission_details_dict['result']

###########################################################
