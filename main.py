import tkinter as tk
from tkinter import ttk, messagebox
from converter_utils import convert_temperature

class TemperatureConverterApp:

    def __init__(self, root):
        self.root = root
        self.root.title("🌡️ Temperature Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Title Label
        title = tk.Label(
            root, text="Temperature Conversion System",
            font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#d72638"
        )
        title.pack(pady=15)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter Temperature:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
        self.temp_entry = tk.Entry(input_frame, width=10, font=("Arial", 11))
        self.temp_entry.grid(row=0, column=1, padx=10)

        # Dropdown Menus
        tk.Label(input_frame, text="From:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, pady=5)
        tk.Label(input_frame, text="To:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=2, pady=5)

        self.from_unit = ttk.Combobox(input_frame, values=["C", "F", "K"], width=5, state="readonly")
        self.from_unit.grid(row=1, column=1)
        self.from_unit.current(0)

        self.to_unit = ttk.Combobox(input_frame, values=["C", "F", "K"], width=5, state="readonly")
        self.to_unit.grid(row=1, column=3)
        self.to_unit.current(1)

        # Result Display
        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333")
        self.result_label.pack(pady=15)

        # Buttons
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack()

        convert_btn = tk.Button(btn_frame, text="Convert", command=self.convert, width=10, bg="#d72638", fg="white", font=("Arial", 10, "bold"))
        convert_btn.grid(row=0, column=0, padx=10)

        reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset, width=10, bg="#0077b6", fg="white", font=("Arial", 10, "bold"))
        reset_btn.grid(row=0, column=1, padx=10)

        exit_btn = tk.Button(btn_frame, text="Exit", command=root.quit, width=10, bg="#444", fg="white", font=("Arial", 10, "bold"))
        exit_btn.grid(row=0, column=2, padx=10)

    def convert(self):
        """Handle conversion logic."""
        try:
            value = float(self.temp_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            # Validation: Absolute zero check
            if from_unit == "C" and value < -273.15:
                raise ValueError("Temperature below absolute zero!")
            if from_unit == "K" and value < 0:
                raise ValueError("Temperature below absolute zero in Kelvin!")

            result = convert_temperature(value, from_unit, to_unit)
            self.result_label.config(
                text=f"{value:.2f}°{from_unit} = {round(result, 2):.2f}°{to_unit}",
                fg="#333333"
            )
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")

    def reset(self):
        """Clear all input and output fields."""
        self.temp_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.from_unit.current(0)
        self.to_unit.current(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
