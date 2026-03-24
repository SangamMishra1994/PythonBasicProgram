# After implementing the SRP
from pathlib import Path
from zipfile import ZipFile


# We have created a separate class so that each class has
# Separate responsibilties.
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


# We have created a separate class so that each class has
# Separate responsibilties.
class ZipFileManager:
    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archieve:
            archieve.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archieve:
            archieve.extractall()


if __name__ == "__main__":
    filename = "example.txt"
    # Managing normal file operations
    file_mgr = FileManager(filename)
    file_mgr.write("Hello SRP!")  # Write
    print(file_mgr.read())  # Read

    # Managing compression operations
    zip_mgr = ZipFileManager(filename)
    zip_mgr.compress()
    zip_mgr.decompress()
