import unittest
from unittest.mock import patch
from ICE2_101000609 import sensor_input, temp_input, temp_sort, temp_min_max, temp_average, main

class TestTemperatureSensor(unittest.TestCase):

    @patch("builtins.input", side_effect=["3"])
    def test_sensor_input_valid(self, mock_input):
        """Test sensor_input with a valid number of sensors."""
        result = sensor_input()
        self.assertEqual(result, 3)

    @patch("builtins.input", side_effect=["-2"])
    def test_sensor_input_negative(self, mock_input):
        """Test sensor_input with a negative number of sensors."""
        result = sensor_input()
        self.assertEqual(result, "Error: Improper Number of Sensors Provided. Please only input a positive integer value.")

    @patch("builtins.input", side_effect=["0"])
    def test_sensor_input_zero(self, mock_input):
        """Test sensor_input with no sensors"""
        result = sensor_input()
        self.assertEqual(result, "Error: Improper Number of Sensors Provided. Please only input a positive integer value.")

    @patch("builtins.input", side_effect=["abc"])
    def test_sensor_input_invalid(self, mock_input):
        """Test sensor_input with an invalid (non-integer) input."""
        result = sensor_input()
        self.assertEqual(result, "Error: Invalid Input, please only input a positive integer value.")

    @patch("builtins.input", side_effect=["9999999999999999999999999999999999999999999999999999999999999999"])
    @patch("builtins.int", side_effect=OverflowError) #forcing an overflow error to occur
    def test_sensor_input_overflow_error(self, mock_int, mock_input):
        """Testing sensor_input handling an OverflowError"""
        result = sensor_input()
        self.assertEqual(result, "Error: Number too large", "sensor_input didn't catch OverflowError correctly")

    @patch("builtins.input", side_effect=["25", "100", "-60", "30"])
    def test_temp_input_out_of_range(self, mock_input):
        """Test temp_input with an out-of-range temperature (-60)."""
        result = temp_input(3)
        self.assertEqual(result, "Error: Temperature is out of valid range for sensor readings")

    @patch("builtins.input", side_effect=["25", "100", "30"])
    def test_temp_input_valid(self, mock_input):
        """Test temp_input with valid temperature readings."""
        result = temp_input(3)
        self.assertEqual(result, [25.0, 100.0, 30.0])

    @patch("builtins.input", side_effect=["apple"])
    def test_temp_input_string_entry(self, mock_input):
        """Test temp_input with a non-numeric temperature entry."""
        result = temp_input(1)
        self.assertEqual(result, "Error: Please only enter numeric values")

    def test_temp_sort(self):
        """Test temp_sort to ensure it correctly sorts temperature values."""
        temps = [30, 10, 25, -5, 100]
        sorted_temps = temp_sort(temps)
        self.assertEqual(sorted_temps, [-5, 10, 25, 30, 100])

    def test_temp_sort_sorted_input(self):
        """Test temp_sort with a list that is already sorted."""
        temps = [-10, 0, 10, 15, 20, 35, 40, 100, 125]
        sorted_temps = temp_sort(temps)
        self.assertEqual(sorted_temps, temps)

    def test_temp_min_max_match(self):
        """Test temp_min_max when there is only one input"""
        temp = [25]
        result = temp_min_max(temp)
        self.assertEqual(result, [25, 25])    

    def test_temp_min_max(self):
        """Test temp_min_max to ensure correct min and max values are extracted."""
        temps = [-5, 10, 25, 30, 100]
        result = temp_min_max(temps)
        self.assertEqual(result, [-5, 100])

    def test_temp_average(self):
        """Test temp_average to ensure the correct average is calculated."""
        temps = [10, 20, 30, 40, 50]
        result_holder = temp_min_max(temps)  
        temp_average(temps, result_holder)  
        self.assertEqual(result_holder, [10, 50, 30.0])
    
    def test_temp_average_single_temp(self):
        """Test temp_average with a single value"""
        temp = [40]
        result_holder = temp_min_max(temp)
        temp_average(temp, result_holder)
        self.assertEqual(result_holder, [40, 40, 40.0])

    def test_temp_average_empty_list(self):
        """Test temp_average with an empty list (shouldn't be possible)"""
        temp = []
        result_holder = []
        with self.assertRaises(ZeroDivisionError):
            temp_average(temp, result_holder)  

    @patch("builtins.input", side_effect=["3", "25", "30", "35"])
    @patch("builtins.print")
    def test_main_function(self, mock_print, mock_input):  
        

        expected_min = 25.0
        expected_max = 35.0
        expected_avg = round((25.0+30.0+35.0)/3, 2)

        DEGREE_SIGN= u'\N{DEGREE SIGN}'

        expected_output = (f"Min: {expected_min}{DEGREE_SIGN}, Max: {expected_max}{DEGREE_SIGN}, Avg: {expected_avg}{DEGREE_SIGN}")
        main()
        printed_statements = [call_args[0][0] for call_args in mock_print.call_args_list]


        self.assertIn(expected_output, printed_statements, f"Expected output '{expected_output}' not found in {printed_statements}")    

if __name__ == '__main__':
    unittest.main()
