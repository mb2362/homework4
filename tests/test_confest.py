"""
This module generates random test data for a calculator application using the Faker library.

It provides a function to create random numbers and operations, which can be used to test
various arithmetic operations (addition, subtraction, multiplication, division).

"""

from faker import Faker

fake = Faker()

def generate_fake_numbers():
    """
    Generate random numbers and a random operation using Faker.

    Returns:
        tuple: A tuple containing two random integers (a, b) and a random operation.
               The operation is randomly selected from ('add', 'subtract', 'multiply', 'divide').
    """
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
    return a, b, operation
