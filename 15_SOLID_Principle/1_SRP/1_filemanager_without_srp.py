# Before implementing the SRP
from pathlib import Path
from zipfile import ZipFile


# This class has more methods which is very confusing as this file
# is responsible for what task. As if now, it perform read90 operation,
# write() operation and along with it also perform compression
# and decompression of file.


class FilManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archieve:
            archieve.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archieve:
            archieve.extractall()


if __name__ == "__main__":
    filename = "[Path of the file]"
    filemanager_object = FilManager()
    filemanager_object.read(filename)
