import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")
        
        self.weight_label = tk.Label(master, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0)
        self.weight_entry = tk.Entry(master)
        self.weight_entry.grid(row=0, column=1)
        
        self.height_label = tk.Label(master, text="Height (m):")
        self.height_label.grid(row=1, column=0)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=1, column=1)
        
        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2)
        
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, columnspan=2)
        
        self.history_button = tk.Button(master, text="View History", command=self.show_history)
        self.history_button.grid(row=4, columnspan=2)
        
        self.data_file = "bmi_data.txt"
        self.data = self.load_data()
        
    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            bmi = weight / (height ** 2)
            category = self.get_category(bmi)
            self.result_label.config(text=f"BMI: {bmi:.2f}, Category: {category}")
            self.save_data(weight, height, bmi, category)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    def get_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def load_data(self):
        data = []
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                for line in f:
                    entry = line.strip().split(",")
                    data.append(entry)
        return data
    
    def save_data(self, weight, height, bmi, category):
        with open(self.data_file, "a") as f:
            f.write(f"{weight},{height},{bmi},{category}\n")
    
    def show_history(self):
        if self.data:
            weights = [float(entry[0]) for entry in self.data]
            bmis = [float(entry[2]) for entry in self.data]
            
            plt.plot(weights, bmis, 'o-')
            plt.xlabel('Weight (kg)')
            plt.ylabel('BMI')
            plt.title('BMI History')
            plt.grid(True)
            plt.show()
        else:
            messagebox.showinfo("Info", "No history data available.")

def main():
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
