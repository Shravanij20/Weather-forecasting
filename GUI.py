######################################
#####################################
#####################################
import tkinter as tk
from tkinter import messagebox
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from PIL import ImageTk, Image

# Dummy training data (replace this with your actual data)
X_train = np.array([[0.1, 10, 20, 5], [0.0, 15, 25, 10], [1.0, 5, 15, 20], [0.5, 0, 10, 15], [0.0, 20, 30, 5]])  # Your feature vectors
y_train = np.array([0, 4, 2, 1, 3])  # Corresponding labels: 0-Drizzle, 1-Fog, 2-Rain, 3-Snow, 4-Sunny

# Train the GBC model
gbc_model = GradientBoostingClassifier()
gbc_model.fit(X_train, y_train)

# Dictionary mapping weather conditions to image files
weather_images = {
    "Drizzle": "C:/weather/Drizzle.jpg",
    "Fog": "C:/weather/Fog.jpg",
    "Rain": "C:/weather/Rain.jpg",
    "Snow": "C:/weather/Snow.jpg",
    "Sunny": "C:/weather/Sunny.jpg"
}

# Function to predict weather based on input features
def predict_weather(features):
    gbc_ans = gbc_model.predict(features.reshape(1, -1))[0]
    if gbc_ans == 0:
        return "Drizzle"
    elif gbc_ans == 1:
        return "Fog"
    elif gbc_ans == 2:
        return "Rain"
    elif gbc_ans == 3:
        return "Snow"
    elif gbc_ans == 4:
        return "Sunny"
    else:
        return "Unknown"

# Function to handle button click event
def predict():
    try:
        # Get input values from the entry fields
        precipitation = float(entry_precipitation.get())
        min_temp = float(entry_min_temp.get())
        max_temp = float(entry_max_temp.get())
        wind_speed = float(entry_wind_speed.get())
        
        input_features = np.array([precipitation, min_temp, max_temp, wind_speed])  # Input features
        predicted_weather = predict_weather(input_features)
        
        # Update the text box with predicted weather
        output_text.delete(1.0, tk.END)  # Clear previous content
        output_text.insert(tk.END, f"The predicted weather is: {predicted_weather}\n")
        
        # Load and display the corresponding image
        image_file = weather_images.get(predicted_weather)
        if image_file:
            image = Image.open(image_file)
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            output_text.image_create(tk.END, image=photo)
            output_text.insert(tk.END, "\n")
            output_text.image = photo
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to resize the background image when the window is resized
def resize_background(event):
    global background_image, canvas
    size = (event.width, event.height)
    resized_image = background_image.resize(size, Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=new_image)
    canvas.image = new_image

# GUI setup
root = tk.Tk()
root.title("Weather Prediction")
root.geometry("800x600")  # Set initial window size
root.resizable(True, True)  # Allow window resizing in both directions

# Add a Canvas widget for background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)  # Fill the entire window and expand with it

# Load background image
background_image = Image.open("C:/weather/weather.png")
background_image = background_image.resize((800, 600), Image.ANTIALIAS)  # Resize the image to fit the canvas
background_image = ImageTk.PhotoImage(background_image)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Bind the window resize event to the function that resizes the background image
root.bind("<Configure>", resize_background)

# Add GUI elements
label_precipitation = tk.Label(root, text="Precipitation:")
label_precipitation.place(relx=0.1, rely=0.1)
entry_precipitation = tk.Entry(root)
entry_precipitation.place(relx=0.25, rely=0.1)

label_min_temp = tk.Label(root, text="Minimum Temperature:")
label_min_temp.place(relx=0.1, rely=0.2)
entry_min_temp = tk.Entry(root)
entry_min_temp.place(relx=0.35, rely=0.2)

label_max_temp = tk.Label(root, text="Maximum Temperature:")
label_max_temp.place(relx=0.1, rely=0.3)
entry_max_temp = tk.Entry(root)
entry_max_temp.place(relx=0.35, rely=0.3)

label_wind_speed = tk.Label(root, text="Wind Speed:")
label_wind_speed.place(relx=0.1, rely=0.4)
entry_wind_speed = tk.Entry(root)
entry_wind_speed.place(relx=0.25, rely=0.4)

button = tk.Button(root, text="Predict", command=predict)
button.place(relx=0.2, rely=0.5)

# Add a text box to display the output
output_text = tk.Text(root, height=10, width=50)
output_text.place(relx=0.1, rely=0.6)

root.mainloop()


import tkinter as tk
from tkinter import messagebox
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from PIL import ImageTk, Image

# Dummy training data (replace this with your actual data)
X_train = np.array([[0.1, 10, 20, 5], [0.0, 15, 25, 10], [1.0, 5, 15, 20], [0.5, 0, 10, 15], [0.0, 20, 30, 5]])  # Your feature vectors
y_train = np.array([0, 4, 2, 1, 3])  # Corresponding labels: 0-Drizzle, 1-Fog, 2-Rain, 3-Snow, 4-Sunny

# Train the GBC model
gbc_model = GradientBoostingClassifier()
gbc_model.fit(X_train, y_train)

# Dictionary mapping weather conditions to image files
weather_images = {
    "Drizzle": "C:/weather/Drizzle.jpg",
    "Fog": "C:/weather/Fog.jpg",
    "Rain": "C:/weather/Rain.jpg",
    "Snow": "C:/weather/Snow.jpg",
    "Sunny": "C:/weather/Sunny.jpg"
}

# Function to predict weather based on input features
def predict_weather(features):
    gbc_ans = gbc_model.predict(features.reshape(1, -1))[0]
    if gbc_ans == 0:
        return "Drizzle"
    elif gbc_ans == 1:
        return "Fog"
    elif gbc_ans == 2:
        return "Rain"
    elif gbc_ans == 3:
        return "Snow"
    elif gbc_ans == 4:
        return "Sunny"
    else:
        return "Unknown"

# Function to handle button click event
def predict():
    try:
        # Get input values from the entry fields
        precipitation = float(entry_precipitation.get())
        min_temp = float(entry_min_temp.get())
        max_temp = float(entry_max_temp.get())
        wind_speed = float(entry_wind_speed.get())
        
        input_features = np.array([precipitation, min_temp, max_temp, wind_speed])  # Input features
        predicted_weather = predict_weather(input_features)
        
        # Update the text box with predicted weather
        output_text.delete(1.0, tk.END)  # Clear previous content
        output_text.insert(tk.END, f"The predicted weather is: {predicted_weather}\n")
        
        # Load and display the corresponding image
        image_file = weather_images.get(predicted_weather)
        if image_file:
            image = Image.open(image_file)
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            output_image.configure(image=photo)
            output_image.image = photo
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Weather Prediction")
root.geometry("800x600")  # Set initial window size
root.resizable(True, True)  # Allow window resizing in both directions

# Add GUI elements
label_precipitation = tk.Label(root, text="Precipitation:")
label_precipitation.place(relx=0.1, rely=0.1)
entry_precipitation = tk.Entry(root)
entry_precipitation.place(relx=0.25, rely=0.1)

label_min_temp = tk.Label(root, text="Minimum Temperature:")
label_min_temp.place(relx=0.1, rely=0.2)
entry_min_temp = tk.Entry(root)
entry_min_temp.place(relx=0.35, rely=0.2)

label_max_temp = tk.Label(root, text="Maximum Temperature:")
label_max_temp.place(relx=0.1, rely=0.3)
entry_max_temp = tk.Entry(root)
entry_max_temp.place(relx=0.35, rely=0.3)

label_wind_speed = tk.Label(root, text="Wind Speed:")
label_wind_speed.place(relx=0.1, rely=0.4)
entry_wind_speed = tk.Entry(root)
entry_wind_speed.place(relx=0.25, rely=0.4)

button = tk.Button(root, text="Predict", command=predict)
button.place(relx=0.2, rely=0.5)

# Add a text box to display the output
output_text = tk.Text(root, height=10, width=50)
output_text.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.9)

# Add an image widget to display weather image
output_image = tk.Label(root)
output_image.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.6)

root.mainloop()