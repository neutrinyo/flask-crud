import unittest
import sys
from datetime import datetime
from openpyxl import Workbook
import pandas as pd


from ordersystem.services import generate_xlsx_report

class TestXlsxReport(unittest.TestCase):
    datetime_str = '09/19/22 13:55:26'
    datetime_str_2 = '09/18/22 13:55:26'

    this_time = datetime.strptime(datetime_str_2, '%m/%d/%y %H:%M:%S')
    other_time = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    def test_correct_input_fields(self):
        input_dict = [{ 
            "id": 1, 
            "creation_date": self.other_time,
            "status": "New",
            "name": "1",
            "description": "1",
        }, {
            "id": 2,
            "creation_date": self.this_time,
            "status": "Completed",
            "name": "2",
            "description": "2",
        }, {
            "id": 3,
            "creation_date": self.this_time,
            "status": "In progress",
            "name": "2",
            "description": "2",
            }]

        function_output = generate_xlsx_report(input_dict)
        correct_output = Workbook()
        # TODO: initialize a workbook with the data mentioned above and proper colors in rows. compare the two.

        pass

    
