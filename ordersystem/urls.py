from flask import request
from .app import app
from .controllers import list_all_orders, delete_order, update_order, create_order, retrieve_order, bulk_update_orders, get_statistics, get_xlsx_report


@app.route("/orders", methods=["GET", "POST"])
def list_and_create():
    '''
    list_and_create - URL route function handling basic order operations on unspecified orders - creation of an entry and fetching the contents of the entire database. 
    Handles GET and POST methods
    In CRUD terms - Create and Read.

    Request inputs for creation of order (POST):
    - name - string fulfilling the specifications described for Order.name in models.py. Required field.
    - description - string fulfilling the specifications described for Order.description in models.py. Required field.
    '''
    if request.method == "GET":
        return list_all_orders()
    if request.method == "POST":
        return create_order()
    else: 
        return "Method not allowed.", 400

    
@app.route("/orders/<order_id>", methods=["GET", "PUT", "DELETE"])
def retrieve_update_and_remove(order_id: int):
    '''
    retrieve_update_and_remove - URL route function handling basic order operations on specified orders. Handles GET, PUT, and DELETE methods. 
    Retrieves a particular entry, updates and deletes it.
    In CRUD terms - Read, Update, Delete.
    For details on each function called refer to controllers.py.

    Input:
    - order_id - integer. Id of relevant order, passed through the <order_id> argument in the URL.
    - for update_order - same inputs as for create_order, but they're optional. Status change also allowed through a status argument with a valid status string as a value.
    '''
    if request.method == "GET":
        return retrieve_order(order_id) 
    if request.method == "PUT":
        return update_order(order_id)
    if request.method == "DELETE":
        return delete_order(order_id)
    else:
        return "Method not allowed.", 400
    

@app.route("/orders/bulk", methods = ["POST"])
def bulk_update():
    '''
    bulk_update - URL  route function handling bulk status updates. Only handles POST requests.
    For details on each function called refer to controllers.py.

    Request inputs:
    - id_list - comma separated, whitespace free string of integers. Ids of the entries the user wants to update.
    - status_list - comma separated, whitespace free list of valid statuses (refer to models.py for allowed values). Maps 1 to 1 with id_list. 
    List of statuses the user wants to apply to the entries with ids mentioned in id_list. 
    '''
    if request.method != "POST":
        return "Method not allowed.", 400
    
    return bulk_update_orders()


@app.route("/orders/stats", methods = ["GET"])
def get_order_stats():
    '''
    get_order_stats - URL route function returning statistics about the database. Only handles GET requests. 
    Fetches the entirety of the database and computes the following statistics: total entry number,
    oldest entry, newest entry, number of entries per status.
    '''
    if request.method != "GET":
        return "Method not allowed.", 400
    
    return get_statistics()


@app.route("/orders/report", methods = ["GET"])
def generate_report():
    '''
    generate_report - URL route function returning an .xlsx report about the contents of the database.
    Only handles GET requests.
    Fetches the entirety of the database and puts it into an .xlsx file, colors the rows of the file in relation to the entry's status.
    '''
    if request.method != "GET":
        return "Method not allowed.", 400
    
    return get_xlsx_report()