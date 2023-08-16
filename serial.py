"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.num = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.num}>"

    def generate(self):
        """generates the next number in the sequence"""
        self.num += 1
        return self.num - 1

    def reset(self):
        """This function resets the number to the original number passed in"""
        self.num = self.start
