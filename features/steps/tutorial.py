from behave import *
import requests
import json


api_url = "http://127.0.0.1:5000/getTask"
file = open('C:\\Users\\HP\\PycharmProjects\\behavetest\\features\\steps\\content.json', 'r')
json_text = file.read()
l= eval(json_text)
request_json = json.dumps(l)

response = requests.post(api_url, request_json)
print(response.content == b'No such User')
@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    api_url = "https://reqres.in//api/users?page=2"
    json_text = '{"name": "Arvind"}'
    request_json = json.loads(json_text)

    response = requests.post(api_url, request_json)
    print("rfdsdfds")
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False