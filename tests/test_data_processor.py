import unittest
from unittest.mock import Mock
import os
from data_processor import DataProcessor

# filepath: /home/karci/KAproject/test_data_processor.py


class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.txt"
        self.mock_logger = Mock()
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_does_not_exist(self):
        processor = DataProcessor(data_file=self.test_file, logger=self.mock_logger)
        processor.read_file()
        self.mock_logger.log.assert_called_with("An error occurred while reading the file: File does not exist.")
        self.assertNotIn(
            ("Task finished. File read completed.",),
            [call[0] for call in self.mock_logger.log.call_args_list]
        )

    def test_file_is_empty(self):
        with open(self.test_file, 'w', encoding='utf-8') as file:
            pass  # Create an empty file
        processor = DataProcessor(data_file=self.test_file, logger=self.mock_logger)
        processor.read_file()
        self.mock_logger.log.assert_any_call(f"Error: The file {self.test_file} is empty.")
        self.mock_logger.log.assert_any_call("Task finished. File read completed.")


    def test_file_with_content(self):
        content = "Line 1\nLine 2\nLine 3"
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write(content)
        processor = DataProcessor(data_file=self.test_file, logger=self.mock_logger)
        processor.read_file()
        self.mock_logger.log.assert_any_call("No of lines 3 and characters 20 in the file")

    def test_oserror_handling(self):
        processor = DataProcessor(data_file="/invalid/path/to/file.txt", logger=self.mock_logger)
        processor.read_file()
        self.mock_logger.log.assert_any_call("An error occurred while reading the file: File does not exist.")


if __name__ == "__main__":
    unittest.main()