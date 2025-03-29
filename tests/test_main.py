import unittest
from unittest.mock import patch, Mock, call
from main import main
from data_retrieval import DataRetrieval
import requests

# filepath: /home/karci/KAproject/test_main.py

class TestDataRetrievalMethods(unittest.TestCase):
    def setUp(self):
        self.mock_logger = Mock()
        self.mock_processor = Mock()
        self.data_file = "test_file.txt"
        self.data_type = "json"
        self.url = "http://example.com/api/data"
        self.data_retrieval = DataRetrieval(
            data_file=self.data_file,
            data_type=self.data_type,
            url=self.url,
            logger=self.mock_logger,
            processor=self.mock_processor
        )

    @unittest.mock.patch("data_retrieval.requests.get")
    @unittest.mock.patch("data_retrieval.os.path.exists")
    def test_retrieve_data_success(self, mock_exists, mock_get):
        # Mock successful HTTP response
        mock_exists.return_value = True
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1}, {"id": 2}]

        # Mock file content
        with unittest.mock.patch("builtins.open", unittest.mock.mock_open(read_data="")):
            content, retrieved_data = self.data_retrieval.retrieve_data()

        self.assertEqual(retrieved_data, [{"id": 1}, {"id": 2}])
        self.assertEqual(content, "")
        self.mock_logger.log.assert_called_with("Task started.")

    @unittest.mock.patch("data_retrieval.requests.get")
    def test_retrieve_data_http_failure(self, mock_get):
        # Mock HTTP request failure
        mock_get.side_effect = requests.exceptions.RequestException("HTTP Error")

        content, retrieved_data = self.data_retrieval.retrieve_data()

        self.assertEqual(retrieved_data, [])
        self.assertEqual(content, "")
        self.mock_logger.log.assert_any_call("HTTP request failed: HTTP Error")
 
    @unittest.mock.patch("data_retrieval.requests.get")
    def test_retrieve_data_invalid_json(self, mock_get):
        # Mock invalid JSON response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.side_effect = ValueError("Invalid JSON")

        content, retrieved_data = self.data_retrieval.retrieve_data()

        self.assertEqual(retrieved_data, [])
        self.assertEqual(content, "")
        self.mock_logger.log.assert_any_call("Data validation error: Invalid JSON")

    @unittest.mock.patch("data_retrieval.os.path.exists")
    def test_retrieve_data_missing_file(self, mock_exists):
        # Mock missing file
        mock_exists.return_value = False

        with unittest.mock.patch("builtins.open", unittest.mock.mock_open()):
            content, retrieved_data = self.data_retrieval.retrieve_data()

        self.assertEqual(content, "")
        self.mock_logger.log.assert_any_call(f"File {self.data_file} does not exist. Proceeding with empty content.")

    @unittest.mock.patch("data_retrieval.os.path.exists")
    def test_write_data(self, mock_exists):
        # Mock file existence
        mock_exists.return_value = True

        # Mock file writing
        with unittest.mock.patch("builtins.open", unittest.mock.mock_open()) as mock_file:
            self.data_retrieval.write_data("", [{"id": 1}, {"id": 2}])

        mock_file().write.assert_any_call("{'id': 1}\n")
        mock_file().write.assert_any_call("{'id': 2}\n")
        self.mock_logger.log.assert_any_call("Added 2 new lines and 0 repeats occurred")

    def test_write_data_no_content(self):
        # Test handling of None content or retrieved_data
        self.data_retrieval.write_data(None, None)
        self.mock_logger.log.assert_called_with("No data to write due to previous errors")
if __name__ == "__main__":
    unittest.main()