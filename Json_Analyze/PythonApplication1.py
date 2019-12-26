import json
import sys
#print(sys.version)
import requests
# Get Json from website
resp = requests.get("https://api.github.com/events")
dic = dict()
for index in resp.json():
       #print(index.items())
       for k,v in index.items():
           dic[k] = None
print(dic)
#print(resp.json())
#print(type(resp.json()))

"""
resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200: 
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))

# The shortcut
resp = requests.post('https://todolist.example.com/tasks/', json=task)
# The equivalent longer version
resp = requests.post('https://todolist.example.com/tasks/',
                     data=json.dumps(task),
                     headers={'Content-Type':'application/json'} 
print("Should not be shown")
"""
print("Show")
# todo.py
def _url(path):
    return 'https://todo.example.com' + path

def get_tasks():
    return requests.get(_url('/tasks/'))

def describe_task(task_id):
    return requests.get(_url('/tasks/{:d}/'.format(task_id)))
def add_task(summary, description=""):
      return requests.post(_url('/tasks/'), json={
        'summary': summary,
        'description': description,
        })

def task_done(task_id):
    return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

def update_task(task_id, summary, description):
     url = _url('/tasks/{:d}/'.format(task_id))
     return requests.put(url, json={
        'summary': summary,
        'description': description,
        }) 


#import todo
#json loads -> returns an object from a string representing a json object.
#json dumps -> returns a string representing a json object from an object. (json.dumps(data, ensure_ascii=False, indent=4))
#load and dump -> read/write from/to file instead of string
