import tkinter as tk
from tkinter import font


def convert_altitude():
  altitude = float(entry_altitude.get())
  input_unit = variable_input.get()
  output_unit = variable_output.get()

  if input_unit == "km":
    altitude = altitude * 1000
  elif input_unit == "ft":
    altitude = altitude * 0.3048
  elif input_unit == "m":
    pass
  else:
    result = "Invalid input unit. Please enter km, ft, or m."

  if output_unit == "km":
    result = altitude / 1000
  elif output_unit == "ft":
    result = altitude / 0.3048
  elif output_unit == "m":
    result = altitude
  else:
    result = "Invalid output unit. Please enter km, ft, or m."

  label_result.config(text=result)


root = tk.Tk()
root.title("Altitude Converter")

# styling
custom_font = font.Font(family='Helvetica', size=14)

label_altitude = tk.Label(root, text="Enter altitude:", font=custom_font)
entry_altitude = tk.Entry(root, font=custom_font)

variable_input = tk.StringVar(root)
variable_input.set("m")

variable_output = tk.StringVar(root)
variable_output.set("m")

unit_options = ["km", "ft", "m"]

unit_input_dropdown = tk.OptionMenu(root, variable_input, *unit_options)
unit_output_dropdown = tk.OptionMenu(root, variable_output, *unit_options)
unit_input_dropdown.config(font=custom_font)
unit_output_dropdown.config(font=custom_font)

label_from = tk.Label(root, text="from:", font=custom_font)
label_convert_to = tk.Label(root, text="convert to:", font=custom_font)

label_result = tk.Label(root, text="", font=custom_font)

convert_button = tk.Button(root,
                           text="Convert",
                           command=convert_altitude,
                           font=custom_font)

# grid layout
label_from.grid(row=0, column=0, pady=10)
unit_input_dropdown.grid(row=0, column=1, pady=10)
label_altitude.grid(row=1, column=0, pady=10)
entry_altitude.grid(row=1, column=1, pady=10)
label_convert_to.grid(row=2, column=0, pady=10)
unit_output_dropdown.grid(row=2, column=1, pady=10)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)
label_result.grid(row=4, column=0, columnspan=2, pady=10)
