from flask import request, send_file, Response
from . import db
from io import BytesIO


from .services import compute_statistics, generate_xlsx_report, parse_bulk_order_inputs
from .models import Order

def list_all_orders() -> list:
    orders = Order.query.all()
    response = []

    for order in orders:
        response.append(order.toDict())

    return response


def create_order() -> dict:
    request_form = request.args.to_dict()

    try: 
        new_order = Order(
            name = request_form['name'],
            description = request_form['description'],
            status = 'New'
        )
    except KeyError as e:
        return f"Order intialization has failed due to missing key(s): {e}.",  400

    db.session.add(new_order)
    db.session.commit()

    response = Order.query.get(new_order.id).toDict()
    return response


def retrieve_order(order_id: int) -> dict:
    try:
        response = Order.query.get(order_id).toDict()
    except AttributeError:
        return f"Requested id '{order_id}' does not exist on the database.", 400
    return response


def update_order(order_id: int) -> dict:
    request_form = request.args.to_dict()
    order = Order.query.get(order_id)
 
    if request_form.get('name') is not None:
        order.name = request_form['name']
        
    if request_form.get('description') is not None:    
        order.description = request_form['description']
    
    if request_form.get('status') is not None: 
        try:   
            order.status = request_form['status']
        except ValueError as ve:
            return f'{ve}', 400

    db.session.commit()

    response = Order.query.get(order_id).toDict()
    return response


def delete_order(order_id: int) -> str:
    query = Order.query.filter_by(id=order_id)
    if len(query.all()) == 0:
        return f"Order of id {order_id} does not exist on the database and therefore cannot be deleted.", 400
    
    query.delete()
    db.session.commit()

    return f'Account with id {order_id} has been deleted.'


def bulk_update_orders() -> dict:
    request_form = request.args.to_dict()
    response = []
    
    id_numbers, status_list = parse_bulk_order_inputs(request_form)

    if status_list == 400:
        return f"{id_numbers}", 400
    
    query = Order.query.filter(Order.id.in_(id_numbers))
    query_length = len(query.all())

    if query_length != len(id_numbers):
        return "One of the provided ids does not exist in the database.", 400
    
    id_status_pairs = dict(zip(id_numbers, status_list))

    for order in query.all():
        try:
            order.status = id_status_pairs[order.id]
            response.append(order.toDict())
        except ValueError as ve:
            return f"{ve}", 400

    db.session.commit()
    return response


def get_statistics() -> str:
    order_dict = list_all_orders()
    try:
        database_size, oldest_entry_id, oldest_entry_date, newest_entry_id, newest_entry_date, status_count = compute_statistics(order_dict)
    except KeyError as ke:
        return f"Not enough arguments to calculate the statistics: {ke} is missing. The database is either empty or has a schema incompatible with this method.", 400
    except ValueError as ve:
        return f"One of the fields has an incorrect value needed for computations: {ve}", 400
    return f"The database has a total of {database_size} entries. \nThe oldest entry has an id of {oldest_entry_id} and been created on: {oldest_entry_date}.\nThe newest entry has an id of {newest_entry_id} and been created on: {newest_entry_date}. \nCounts of each status: \n {status_count}"
    


def get_xlsx_report() -> Response:
    order_dict = list_all_orders()
    workbook = generate_xlsx_report(order_dict)
    file_stream = BytesIO()

    workbook.save(file_stream)
    file_stream.seek(0)

    return send_file(file_stream, as_attachment=True, download_name='order-report.xlsx')