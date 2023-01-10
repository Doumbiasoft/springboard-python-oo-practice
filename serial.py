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

    def __init__(self, start=100):
        """Generator initialization  """
        self.start = start
        self.count = 0

    def generate(self):
        """this method generates the next number"""
        num = self.start + self.count
        self.count += 1
        return num

    def reset(self):
        """this method clears generator"""
        self.count = 0
