import argparse
from logger import Logger
from data_retrieval import DataRetrieval
from data_processor import DataProcessor

def main(args):
    logger = Logger()
    data_types = ["posts", "comments", "albums", "photos", "todos", "users"]
    data_file = f"data/{data_type}.txt"
    url = f"https://jsonplaceholder.typicode.com/{data_type}"
    
    if args.data_type:
        data_type = args.data_type.strip().lower()
    else:
        while True:
            data_type = input("Enter the data type - posts, comments, albums, photos, todos, users (esc to exit): ").strip().lower()
            if data_type == 'esc':
                print("Exiting the program.")
                return
            if data_type in data_types:
                break
            else:
                logger.log(f"Invalid {data_type} data type. Please enter a valid data type.")
    
    logger.log(f"Processing {data_type} data")
    processor = DataProcessor(data_file, logger)
    retriever = DataRetrieval(data_file, data_type, url, processor, logger)
    content, retrieved_data = retriever.retrieve_data()
    retriever.write_data(content, retrieved_data)
    processor.read_file()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process some data types.")
    parser.add_argument('--data_type', type=str, help='The type of data to process (posts, comments, albums, photos, todos, users)')
    args = parser.parse_args()
    main(args)