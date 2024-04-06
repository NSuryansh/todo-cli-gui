import PySimpleGUI as sg
import maker_archive

file_text = sg.Text('Select files')
files_input = sg.Input(key="input_files")
files_browse = sg.FilesBrowse('Select', key="files")

folder_text = sg.Text('Select files')
folder_input = sg.Input(key="input_folder")
folder_browse = sg.FolderBrowse('Select', key="folder")

convert_button = sg.Button("Convert")
output_text = sg.Text("", key="output_text")

left_column = sg.Column([[file_text], [folder_text]])
middle_column = sg.Column([[files_input], [folder_input]])
right_column = sg.Column([[files_browse], [folder_browse]])

window = sg.Window("Files Compressor", layout=[[left_column, middle_column, right_column], [convert_button, output_text]])

while True:
    event,  data = window.read()
    file_path = data["files"].split(";")
    window["input_files"].update(value=file_path)
    folder = data["folder"]
    window["input_folder"].update(value=folder)
    maker_archive.archiving(file_path, folder)
    window["output_text"].update(value="Compression Sucesfull")


window.close()
