import unittest
import sys
from datetime import datetime
from numpy import int64

from ordersystem.services import compute_statistics

class TestStatisticsComputation(unittest.TestCase):
    datetime_str = '09/19/22 13:55:26'
    datetime_str_2 = '09/18/22 13:55:26'

    this_time = datetime.strptime(datetime_str_2, '%m/%d/%y %H:%M:%S')
    other_time = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

    def test_correct_input(self):
        input_dict = [{ 
            "id": 1, 
            "creation_date": self.other_time,
            "name": "1",
            "description": "1",
            "status": "New"
        }, {
            "id": 2,
            "creation_date": self.this_time,
            "name": "2",
            "description": "2",
            "status": "Completed"
        }]

        function_output = list(compute_statistics(input_dict))
        correct_output = [2, int64(2), "2022.09.18, 13:55", int64(1), "2022.09.19, 13:55", "statuscount\n0Completed1\n1New1"]
        function_output[5] = function_output[5].replace(" ", "")
        self.assertEqual(function_output, correct_output)

    
    def test_empty_database(self):
        input_dict = []
        
        with self.assertRaises(KeyError) as cm:
            compute_statistics(input_dict)
        
        self.assertEqual(str(cm.exception), "'status'")


    def test_incorrect_date(self):
        input_dict = [{ 
            "id": 1, 
            "creation_date": 1,
            "name": "1",
            "description": "1",
            "status": "New"
        },]
        
        with self.assertRaises(ValueError) as cm:
            compute_statistics(input_dict)

        self.assertEqual(str(cm.exception), 'Given date string "1" not likely a datetime, at position 0')