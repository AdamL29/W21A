import json
from flask import Flask, request
from dbhelper import run_statement

app = Flask(__name__)

@app.get("/api/item")
def get_item():
    result = run_statement("CALL get_items")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json    
    else:
        return "Sorry, something went wrong!"

@app.post('/api/items')
def add_item():
    item_name = request.json.get('itemName')
    if item_name == None:
        return "You must specify an item name."
    result = run_statement("CALL add_item(?)", [item_name])
    if result == None:
        return "Success!!"
    else:
        return "Something went terribly wrong with adding."

@app.patch('/api/items')
def edit_item():
    item_update = request.json.get('itemUpdate')
    if item_update == None:
        return "You must specify an item name."
    result = run_statement("CALL edit_item(?)", [item_update])
    if result == None:
        return "Success?!"
    else:
        return "Something went terribly wrong with editing."

@app.delete('/api/items')
def delete_item():
    item_id = request.json.get('itemId')
    if item_id == None:
        return "You must specify an item Id."
    result = run_statement("CALL delete_item(?)", [item_id])
    if result == None:
        return "Success!"
    else:
        return "Something went terribly wrong with the deletion."

@app.get("/api/employee")
def get_employee():
    result = run_statement("CALL get_employee")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        return "Sorry, something went wrong!"

@app.post('/api/employee')
def add_employee():
    employee_name = request.json.get('employeeName')
    if employee_name == None:
        return "You must specify an employee name."
    result = run_statement("CALL add_employee(?)", [employee_name])
    if result == None:
        return "Success!!"
    else:
        return "Something went terribly wrong with adding."

@app.patch('/api/employee')
def edit_employee():
    employee_update = request.json.get('employeeUpdate')
    if employee_update == None:
        return "You must specify an employee name."
    result = run_statement("CALL edit_employee(?)", [employee_update])
    if result == None:
        return "Success?!"
    else:
        return "Something went terribly wrong with editing."

@app.delete('/api/employee')
def delete_employee():
    employee_id = request.json.get('employeeId')
    if employee_id == None:
        return "You must specify an employee Id."
    result = run_statement("CALL delete_employee(?)", [employee_id])
    if result == None:
        return "Success!"
    else:
        return "Something went terribly wrong with the deletion."


app.run(debug = True)