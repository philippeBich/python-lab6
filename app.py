from flask import Flask, jsonify, Response, request
import json
import database



app = Flask(__name__)
tasks=[]

for id in database.getTasksId():
    task={'name':id, 'text':database.getText(id), 'urgency':database.getUrgency(id)}
    tasks.append(task)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tasks')
def api_tasks():
    return jsonify(tasks)


@app.route('/tasks/<id>')
def api_task(id):
    task = [u for u in tasks if u['name'] == id]
    if len(task) == 1:
        return jsonify(task)
    else:
        response = jsonify({ 'message': "Invalid id "+id })
        response.status_code = 404
        return response


@app.route('/tasks', methods=['POST'])
def api_create_task():
    if request.headers['Content-Type'] == 'application/json':
        new_task = request.json
        tasks.append(new_task)
        database.insertTask(new_task)
        return "Task successfully created!"

    else:
        response = jsonify({ 'message': "Invalid Request"})
        response.status_code = 404
        return response


@app.route('/tasks/delete', methods=['POST'])
def api_delete_task():
    id=request.json

    task=None
    for u in tasks:

        if u['name'] == id:
            task=u

    if task != None:
        tasks.remove(task)
        database.deleteTask(task)
        response = jsonify({'message': "Successfully deleted " + str(id)})
        response.status_code = 200
        return response
    else:
        response = jsonify({ 'message': "Invalid id "+ str(id) })
        response.status_code = 404
        return response


@app.route('/tasks/update', methods=['POST'])
def api_update_task():
    task=request.json
    flag=False
    taskTmp=None

    for u in tasks:
        if u['name'] == task['name']:
            u['text'] = task['text']
            u['urgency'] = task['urgency']
            taskTmp=u
            flag=True

    if flag==True:
        database.updateTask(taskTmp)
        response = jsonify({'message': "Successfully updated " + str(task['name'])})
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': "id not in the database "})
        response.status_code = 404
        return response


if __name__ == '__main__':
    app.run()