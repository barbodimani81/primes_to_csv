import logging


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def logger_decorator(function):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(message)s')
        logger = logging.getLogger()
        logger.info(f"Function started")
        result = function(*args, **kwargs)
        logger.info(f"Function finished")
        return result

    return wrapper


@logger_decorator
def primes_to_file():
    n = int(input("Enter a number: "))
    filename = "prime.txt"
    with open(filename, "w") as file:
        for i in range(2, n):
            if is_prime(i):
                file.write(str(i) + "\n")
    print(f"Prime numbers less than {n} have been written to {filename}")


def main():
    primes_to_file()


if __name__ == "__main__":
    main()