import tkinter as tk
import requests

def actualweather(city):
    API_KEY = "aba2b8c272b613c1dbe5078a1340718d"
    # city=input("Enter a city: ")

    base_url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    weather_data=requests.get(base_url).json()
    return weather_data
    # pprint(weather_data)

def process_input():
    input_text = entry.get()  # Get text from the input widget
    weather_data=actualweather(input_text)
    output_text = "Temperature in "+input_text+" is : "+ str(weather_data['main']['temp'])+" C"+"\n"+"Humidity in "+input_text+" is : "+ str(weather_data['main']['humidity'])+" %" +"\n"+"Feels Like in "+input_text+" is : "+ str(weather_data['main']['feels_like'])+" C"+"\n"+"Pressure in "+input_text+" is : "+ str(weather_data['main']['pressure'])+" mBar"+"\n"+"Maximum temperature in "+input_text+" is : "+ str(weather_data['main']['temp_max'])+" C"+"\n"+"Minimum temperature in "+input_text+" is : "+ str(weather_data['main']['temp_min'])+" C"+"\n"

    text.insert(tk.END, output_text + "\n")  # Insert text into the output widget
    # entry.delete(0, tk.END)  # Clear the input widget

# Create the main window
window = tk.Tk()
window.title("Weather details")
window.configure(bg="light blue")

# Create the input widget
label = tk.Label(window, text="Enter the name of city:")
label.place(x=137,y=1)

# Create the input widget
entry = tk.Entry(window)
entry.pack()

# Create the output widget
text = tk.Text(window)
text.pack()

# Create a button to process the input
button = tk.Button(window, text="Process", command=process_input)
button.pack()

# Start the main event loop
window.mainloop()


































      
























































