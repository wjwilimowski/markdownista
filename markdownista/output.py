from abc import ABC, abstractmethod


class Output(ABC):
    @abstractmethod
    def write(self, line):
        ...


class BufferedOutput(Output):
    def __init__(self):
        self.lines = []

    def write(self, line):
        self.lines.append(line)

    def print(self, *, file=None):
        for line in self.lines:
            print(line, file=file)


class PrintOutput(Output):
    def __init__(self, file=None):
        self.file = file

    def write(self, line):
        print(line, file=self.file)
