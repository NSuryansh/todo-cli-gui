import PySimpleGUI as sg


input_text_feet = sg.Text("Enter Feet")
input_box_feet = sg.InputText(tooltip="Enter Feet", key="Feets")

input_text_inches = sg.Text("Enter Inches")
input_box_inches = sg.InputText(tooltip="Enter Inches", key="Inches")

convert_button = sg.Button("Convert")

meters = sg.Text("", key="output")

layout =[[input_text_feet, input_box_feet], [input_text_inches, input_box_inches],
                                       [convert_button, meters] ]

window = sg.Window("Convertor", layout=layout)



while True:
    event, data = window.read()

    match event:
        case "Convert":

            feet = float(data["Feets"])
            inches = float(data["Inches"])

            meters = feet*0.3048 + inches*0.0254

            window["output"].update(value=meters)

        case sg.WINDOW_CLOSED:
            break

window.close()
