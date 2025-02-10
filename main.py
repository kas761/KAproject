import argparse
from logger import Logger
from data_retrieval import DataRetrieval
from data_processor import DataProcessor

def main():
    data_types = ["posts", "comments", "albums", "photos", "todos", "users"]
    while True:
        data_type = input("Enter the data type - posts, comments, albums, photos, todos, users: ").strip().lower()
        if data_type == 'esc':
            print("Exiting the program.")
            break
        elif data_type in data_types:
            data_file = f"data/{data_type}.txt"
            url = f"https://jsonplaceholder.typicode.com/{data_type}"
            logger = Logger()
            processor = DataProcessor(data_file, logger)
            retriever = DataRetrieval(data_file, url, processor, logger)
            retriever.retrieve_data()
            processor.read_file()
        else:
            print("Invalid data type. Please enter a valid data type.")

if __name__ == '__main__':
    main()