import PySimpleGUI as sg
from zipcreator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key = "Files")


label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="Folder")

compress_button = sg.Button("Compress")
output_label = sg.Text()

window = sg.Window("File compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])

while True:
    event, values = window.read()
    print (event, values)
    filepaths = values["Files"].split(";")
    folder = values["Folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed")

window.close()