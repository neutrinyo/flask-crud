from ..controllers import parse_bulk_order_inputs

def test_dummy():
    assert True

def test_correct_input():
        input_dict = {
            "id_list": "1,2,3",
            "status_list": "New,New,Completed"
        }
        correct_output = ([1, 2, 3], ["New", "New", "Completed"])
        function_output = parse_bulk_order_inputs(input_dict)

        assert correct_output == function_output


def test_only_status_list():
        input_dict = {
            "status_list": "New,New,Completed"
        }
        correct_output = ("Missing required argument: 'id_list'", 400)

        assert parse_bulk_order_inputs(input_dict) == correct_output


def test_only_id_list():
    input_dict = {
        "id_list": "1,2,3"
    }
    correct_output = ("Missing required argument: 'status_list'", 400)

    assert parse_bulk_order_inputs(input_dict) == correct_output

    
def test_non_int_in_id_list():
    input_dict = {
        "id_list": "New,New,Completed",
        "status_list": "New,New,Completed"
    }
    correct_output = ('One of the input lists has an invalid value: invalid literal for int() with '"base 10: 'New'", 400)

    assert parse_bulk_order_inputs(input_dict) == correct_output


def test_unequal_list_lengths():
    input_dict = {
        "id_list": "1,2,3",
        "status_list": "New,New"
    }
    correct_output = ("Unequal lengths of status and id lists.", 400)

    assert parse_bulk_order_inputs(input_dict) == correct_output