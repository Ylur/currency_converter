import sys

from client import convert_value

if __name__ == "__main__":
    value = int(sys.argv[1])

    new_value = convert_value(value)
    print(f'{value} USD = {new_value} RUB')
