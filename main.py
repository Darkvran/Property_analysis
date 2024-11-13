from data_parser import DataParser
import sys

def main():
    data_parser = DataParser()
    response = data_parser.get_advertisements()
    print(response)


if __name__ == "__main__":
        main()

