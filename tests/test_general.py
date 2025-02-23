import os
import json
import pytest
from unittest.mock import MagicMock
from logger import Logger
from data_processor import DataProcessor
from data_retrieval import DataRetrieval


@pytest.fixture
def logger(tmpdir):
    log_file_path = f"{tmpdir}/test_log.txt"
    return Logger(log_file=log_file_path)


@pytest.fixture
def processor(test_data, logger):
    return DataProcessor(test_data, logger)


@pytest.fixture
def url():
    return MagicMock()


@pytest.fixture
def data_type():
    return "json"


@pytest.fixture
def content():
    return MagicMock()


@pytest.fixture
def test_data():
    return [
        {'userId': 1, 'id': 1, 'title': 'test_title1', 'body': 'test_body1'},
        {'userId': 1, 'id': 2, 'title': 'test_title2', 'body': 'test_body2'},
        {'userId': 2, 'id': 1, 'title': 'test_title3', 'body': 'test_body3'}
    ]


@pytest.fixture
def data_file(test_data, tmpdir):
    data_file = f"{tmpdir}/test_data.json"
    with open(data_file, "w", encoding='utf-8') as file:
        json.dump(test_data, file)
    return data_file


@pytest.fixture
def data_retrieval(logger, processor, tmpdir, data_type, url):
    return DataRetrieval(
        data_file=f'{tmpdir}/test.txt',
        data_type=data_type,
        url=url,
        logger=logger,
        processor=processor
    )


def test_logger(logger):
    logger.log("Test message")
    assert os.path.exists(logger.log_file)


def test_data_retrieve(test_data):
    DataRetrieval.retrieved_data = test_data
    assert DataRetrieval.retrieved_data == test_data


def test_data_write(tmpdir, test_data, data_file, data_type, url, logger, processor):
    data_retrieval = DataRetrieval(
        data_file=f'{tmpdir}/test.txt',
        data_type=data_type,
        url=url,
        logger=logger,
        processor=processor
    )
    with open(data_file, "r", encoding='utf-8') as file_read:
        content = file_read
        retrieved_data = test_data
        data_retrieval.write_data(content, retrieved_data)

    assert "Added 3 new lines and 0 repeats occurred" in open(logger.log_file).read()


def test_read_data_file(data_processor):
    data_processor.read_file
    assert data_processor.process_data() == "Test data"
    