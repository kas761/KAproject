import os
import pytest
from unittest.mock import MagicMock
from logger import Logger
from data_processor import DataProcessor
from data_retrieval import DataRetrieval

@pytest.fixture
def logger():
    return Logger("process_log.txt")

@pytest.fixture
def data_file(tmp_path):
    file = tmp_path / "test_data.txt"
    file.write_text("line1\nline2\nline3")
    return file

@pytest.fixture
def processor(data_file, logger):
    return DataProcessor(data_file, logger)

def test_logger_log(logger):
    logger.log_file = "tests/test_log.txt"
    logger.log("Test log message")
    with open(logger.log_file, "r") as log_file:
        assert "Test log message" in log_file.read()
    os.remove(logger.log_file)

def test_data_processor_read_file(data_file, logger):
    processor = DataProcessor(data_file, logger)
    logger.log = MagicMock()
    processor.read_file()
    logger.log.assert_any_call("The number of lines in the file is: 3 and number of characters is: 17")

def test_data_retrieval_retrieve_data(data_file, processor, logger):
    retriever = DataRetrieval(data_file, "test", "https://jsonplaceholder.typicode.com/posts", processor, logger)
    content, retrieved_data = retriever.retrieve_data()
    assert isinstance(content, str)
    assert isinstance(retrieved_data, list)
    assert len(retrieved_data) > 0

def test_data_retrieval_write_data(data_file, processor, logger):
    retriever = DataRetrieval(data_file, "test", "https://jsonplaceholder.typicode.com/posts", processor, logger)
    content = "line1\nline2\nline3"
    retrieved_data = [{"id": 1, "title": "test post"}]
    retriever.write_data(content, retrieved_data)
    with open(data_file, "r") as file:
        file_content = file.read()
        assert "test post" in file_content
        assert "line1" in file_content
        assert "line2" in file_content
        assert "line3" in file_content