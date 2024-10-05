import time
import random
import sys

class Greeter:
    def __init__(self, name=None):
        self.name = name if name else self.generate_name()

    def generate_name(self):
        # Generates a random name from a set of options
        names = ['User', 'Friend', 'Stranger', 'PCU Tester']
        return random.choice(names)

    def print_hi(self):
        self.log_initialisation()
        self.slow_print("Initialising greeting...\n")
        self.log_greeting()
        time.sleep(1)
        
        if self.should_greet():
            self.slow_print(f"Hi, {self.name}!\n")
        else:
            self.slow_print("Sorry, I don't feel like saying hi right now.\n")

    def should_greet(self):
        # A random condition to decide whether to greet
        return random.choice([True, False])

    def slow_print(self, message, delay=0.05):
        # Prints the message one character at a time
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    
    def log_initialisation(self):
        # Logging method for initialisation
        print("Logging: Greeter initialised with name:", self.name)
    
    def log_greeting(self):
        # Logging method for greeting action
        print("Logging: Greeting function called.")
    
if __name__ == "__main__":
    greeter = Greeter()
    greeter.print_hi()
