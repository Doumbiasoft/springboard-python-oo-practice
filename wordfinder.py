"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:

    """Machine to find random words.

        >>> wf = WordFinder("words.txt")
        235886 words read

        >>> wf.random()
        'puerman'

        >>> wf.random()
        'Ronga'

        >>> wf.random()
        'belomancy'

        >>> wf.random()
        'goldbricker'

    """

    def __init__(self, path):
        self.path = path
        self.words = None
        words_count = self.file_count(self.path)
        print(f"{words_count} words read")

    def file_count(self, path):
        file = open(path)
        self.words = [line.strip() for line in file]
        return len(self.words)

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):

    """Machine to find random words without blank and lines comments.
    
    >>> swf = SpecialWordFinder("words.txt")
    235886 words read

    >>> swf.random() in ["puerman", "belomancy", "goldbricker"]
    False

    """

    def file_count(self, path):
        file = open(path)
        self.words = [line.strip() for line in file if line.strip() and not line.startswith("#")]
        return len(self.words)

