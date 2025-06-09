import tkinter


window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=50, pady=50)


def calculate_bmi():
    height = height_entry.get()
    weight = weight_entry.get()
    if height == "" or weight == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except ValueError:
            result_label.config(text="Enter a valid number!")


def clear_entries():
    weight_entry.delete(0, tkinter.END)
    height_entry.delete(0, tkinter.END)
    result_label.config(text="")



weight_input_label = tkinter.Label(window, text="Enter Your Weight (kg)")
weight_input_label.pack()
weight_entry = tkinter.Entry(window)
weight_entry.pack()
height_input_label = tkinter.Label(window, text="Enter Your Height (cm)")
height_input_label.pack()
height_entry = tkinter.Entry(window)
height_entry.pack()
calculate_button = tkinter.Button(window, text="Calculate",command=calculate_bmi)
calculate_button.pack()
clear_button = tkinter.Button(window, text="Clear",command=clear_entries)
clear_button.pack()
result_label = tkinter.Label(window)
result_label.pack()


def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string


window.mainloop()
