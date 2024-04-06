import zipfile
import pathlib

def archiving(filepath, folder):
    folder_path = pathlib.Path(folder, "compressed.zip")
    with zipfile.ZipFile(folder_path, "w") as archive:

        for files in filepath:
            files = pathlib.Path(files)
            archive.write(files, arcname=files.name)















