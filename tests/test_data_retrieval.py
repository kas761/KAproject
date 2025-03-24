import unittest
from unittest.mock import Mock
from data_retrieval import DataRetrieval

# filepath: /home/karci/KAproject/test_data_retrieval.py

class TestDataRetrievalInit(unittest.TestCase):
    def setUp(self):
        # Mock dependencies
        self.mock_logger = Mock()
        self.mock_processor = Mock()
        self.data_file = "test_file.txt"
        self.data_type = "json"
        self.url = "http://example.com/api/data"

    def test_initialization(self):
        # Initialize the DataRetrieval object
        data_retrieval = DataRetrieval(
            data_file=self.data_file,
            data_type=self.data_type,
            url=self.url,
            logger=self.mock_logger,
            processor=self.mock_processor
        )

        # Assert that all attributes are correctly set
        self.assertEqual(data_retrieval.data_file, self.data_file)
        self.assertEqual(data_retrieval.data_type, self.data_type)
        self.assertEqual(data_retrieval.url, self.url)
        self.assertEqual(data_retrieval.logger, self.mock_logger)
        self.assertEqual(data_retrieval.processor, self.mock_processor)

if __name__ == "__main__":
    unittest.main()