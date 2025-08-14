import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import joblib

# Load the trained model
model = joblib.load("liver_disease_rf_model.pkl")

# Feature list
features = [
    "Age",
    "Gender (1=Male, 0=Female)",
    "Total_Bilirubin",
    "Direct_Bilirubin",
    "Alkphos_Alkaline_Phosphotase",
    "Sgpt_Alamine_Aminotransferase",
    "Sgot_Aspartate_Aminotransferase",
    "Total_Proteins",
    "Albumin",
    "Albumin_and_Globulin_Ratio",
]

# Create modern window
window = ttk.Window(themename="flatly")
window.title("🩺 Liver Disease Prediction Tool")
window.geometry("700x720")

# Title Label
ttk.Label(
    window,
    text="🩺 Liver Disease Prediction Tool",
    font=("Segoe UI", 22, "bold"),
    bootstyle="primary",
).pack(pady=(20, 10))

# Frame for input
form_frame = ttk.Frame(window, padding=10)
form_frame.pack(pady=10)

entries = {}

# Input fields
for feature in features:
    row = ttk.Frame(form_frame)
    row.pack(fill="x", pady=8)

    label = ttk.Label(row, text=feature, font=("Segoe UI", 11), width=30, anchor="w")
    label.pack(side="left")

    entry = ttk.Entry(row, font=("Segoe UI", 11), width=30, bootstyle="secondary")
    entry.pack(side="left", padx=10)
    entries[feature] = entry


# Predict function
def predict():
    try:
        input_values = [float(entries[f].get()) for f in features]
        prediction = model.predict([input_values])[0]
        result = (
            "Not likely to have Liver Disease"
            if prediction == 0
            else "Likely to have Liver Disease"
        )
        messagebox.showinfo("Prediction", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Predict Button
ttk.Button(window, text="Predict", command=predict, bootstyle="success", width=20).pack(
    pady=30
)

# Run the app
window.mainloop()
