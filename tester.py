import requests


# like the caller.py defined during lessons


base_url = 'http://localhost:5000'


def list_tasks():
    url = base_url+'/tasks'
    r = requests.get(url)
    return r.json()


def one_task(id):
    url = base_url + '/tasks/' + id
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None

def add_task(id, text, urgency):
    task = { 'name': id, 'text': text, 'urgency': urgency }
    url = base_url + '/tasks'
    r = requests.post(url, json=task)

def delete_task(id):
    url=base_url+'/tasks/delete'
    r=requests.post(url, json=id)

    return r.status_code

def update_task(id, text, urgency):
    task = { 'name': id, 'text': text, 'urgency': urgency }
    url = base_url + '/tasks/update'
    r = requests.post(url, json=task)
    return r.status_code


if __name__ == '__main__':
    print(list_tasks())
    print(update_task(10, "taskUpdated", 1))
    print(list_tasks())
