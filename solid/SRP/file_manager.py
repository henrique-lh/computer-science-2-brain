from pathlib import Path
from zipfile import ZipFile

class FileManager:
    """
    This class has two different responsibilities:
    * Read and Write in a file
    * Compress and Decompress a file

    For that reason, this violates the SRP principle
    """

    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding = 'utf-8'):
        return self.path.read_text(encoding)

    def write(self, data, encoding = 'utf-8'):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode='w') as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode='r') as archive:
            archive.extractall()