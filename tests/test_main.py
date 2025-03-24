import unittest
from unittest.mock import patch, Mock, call
from main import main

# filepath: /home/karci/KAproject/test_main.py


class TestMain(unittest.TestCase):
    @patch("main.Logger")
    @patch("main.DataRetrieval")
    @patch("main.DataProcessor")
    def test_main_with_valid_argument(self, MockDataProcessor, MockDataRetrieval, MockLogger):
        mock_logger = MockLogger.return_value
        mock_retriever = MockDataRetrieval.return_value
        mock_processor = MockDataProcessor.return_value

        arguments = Mock()
        arguments.data_type = "posts"

        main(arguments)

        mock_logger.log.assert_any_call("Processing posts data")
        MockDataRetrieval.assert_called_with(
            "data/posts.txt", "posts", "https://jsonplaceholder.typicode.com/posts", mock_logger, mock_processor
        )
        mock_retriever.retrieve_data.assert_called_once()
        mock_retriever.write_data.assert_called_once()
        mock_processor.read_file.assert_called_once()

    @patch("builtins.input", side_effect=["comments"])
    @patch("main.Logger")
    @patch("main.DataRetrieval")
    @patch("main.DataProcessor")
    def test_main_with_user_input(self, MockDataProcessor, MockDataRetrieval, MockLogger, mock_input):
        mock_logger = MockLogger.return_value
        mock_retriever = MockDataRetrieval.return_value
        mock_processor = MockDataProcessor.return_value

        arguments = Mock()
        arguments.data_type = None

        main(arguments)

        mock_logger.log.assert_any_call("Processing comments data")
        MockDataRetrieval.assert_called_with(
            "data/comments.txt", "comments", "https://jsonplaceholder.typicode.com/comments", mock_logger, mock_processor
        )
        mock_retriever.retrieve_data.assert_called_once()
        mock_retriever.write_data.assert_called_once()
        mock_processor.read_file.assert_called_once()

    @patch("builtins.input", side_effect=["invalid", "esc"])
    @patch("main.Logger")
    def test_main_with_invalid_user_input(self, MockLogger, mock_input):
        mock_logger = MockLogger.return_value

        arguments = Mock()
        arguments.data_type = None

        main(arguments)

        mock_logger.log.assert_any_call("Invalid invalid data type. Please enter a valid data type.")

    @patch("builtins.input", side_effect=["esc"])
    @patch("main.Logger")
    def test_main_user_exits(self, MockLogger, mock_input):
        mock_logger = MockLogger.return_value

        arguments = Mock()
        arguments.data_type = None

        main(arguments)

        mock_logger.log.assert_not_called()

    @patch("main.Logger")
    @patch("main.DataRetrieval")
    @patch("main.DataProcessor")
    def test_main_calls_all_methods(self, MockDataProcessor, MockDataRetrieval, MockLogger):
        mock_logger = MockLogger.return_value
        mock_retriever = MockDataRetrieval.return_value
        mock_processor = MockDataProcessor.return_value

        arguments = Mock()
        arguments.data_type = "users"

        main(arguments)

        mock_logger.log.assert_any_call("Processing users data")
        mock_retriever.retrieve_data.assert_called_once()
        mock_retriever.write_data.assert_called_once()
        mock_processor.read_file.assert_called_once()


if __name__ == "__main__":
    unittest.main()