import argparse
from logger import Logger
from data_retrieval import DataRetrieval
from data_processor import DataProcessor

data_types = ["posts", "comments", "albums", "photos", "todos", "users"]
URL_BASE = "https://jsonplaceholder.typicode.com"
LOG_FILE = "process_log.txt"


def main(arguments):
    logger = Logger(LOG_FILE)

    if arguments.data_type:
        data_type = arguments.data_type.strip().lower()
    else:
        while True:
            data_type = input(f"Enter data type - {data_types} (esc to exit): ").strip().lower()
            if data_type == 'esc':
                print("Exiting the program.")
                return
            if data_type in data_types:
                break
            logger.log(f"Invalid {data_type} data type. Please enter a valid data type.")

    url = f"{URL_BASE}/{data_type}"
    data_file = f"data/{data_type}.txt"
    logger.log(f"Processing {data_type} data")
    processor = DataProcessor(data_file, logger)
    retriever = DataRetrieval(data_file, data_type, url, logger, processor)
    content, retrieved_data = retriever.retrieve_data()
    retriever.write_data(content, retrieved_data)
    processor.read_file()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process some data types.")
    parser.add_argument('data_type', type=str, nargs='?', help=f"Data types - {data_types}.")
    args = parser.parse_args()
    main(args)
