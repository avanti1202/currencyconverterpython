from tkinter import Tk, ttk
import tkinter as tk
from tkinter import *
from requests import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

root = tk.Tk()
root.geometry("500x520+500+150")
root.title("Currency Converter By Avanti")
root.configure(bg = "pink")
root.resizable(height = FALSE, width =FALSE)

#TOP FRAME
top = Frame(root, width=500, height=90, bg= "purple")
top.grid(row=0, column=0)
f = ("Arial", 20, "bold")

icon = Image.open('C:/internship/mira/Python/task1/t1_currencyconverter/images/converticon.png')
icon = icon.resize((70, 70))
icon= ImageTk.PhotoImage(icon)

app_name = Label(top, image = icon, compound =LEFT, text = "Currency Converter", height =5,padx=3, pady=30, anchor=CENTER, font=f , bg = "purple", fg = "white")
app_name.place(x=50, y=10)

#ROOT FRAME
root = Frame(root, width=500, height=430, bg= "pink")
root.grid(row=1, column=0)
f1 = ("Helvetica", 18, "bold")

lab_amt = Label(root, text = 'Enter amount',font = f1,  bg = "pink",fg = "black")
lab_amt.place(x=20, y = 10)
ent_amt = tk.Entry(root, font = f1,width = 12, relief = "solid")
ent_amt.place(x=250, y = 10)

currency = ['INR', 'EUR', 'RUB','USD', 'GBP', 'CNY']
#From Currency  Dropdown
from_lab = Label(root, text = 'From currency', font = f1, bg = "pink",fg = "black")
from_lab.place(x=20, y = 80)
default_value1 = currency[0]
combo1  =ttk.Combobox(root, width =10, justify=CENTER, font= f1, state="readonly")
combo1.set(default_value1)
combo1['values'] = (currency)
combo1.place(x=250, y = 80)

#To Currency Dropdown
to_lab = Label(root, text = 'To currency', font = f1, bg = "pink",fg = "black")
to_lab.place(x=20, y = 160)
default_value2= currency[2]
combo2  =ttk.Combobox(root, width =10, justify=CENTER, font= f1, state="readonly")
combo2.set(default_value2)
combo2['values'] = (currency)
combo2.place(x=250, y = 160)

#Function to convert Currency  
def convert():
	try:
		amount = ent_amt.get()
		from_currency = combo1.get()
		to_currency = combo2.get()

		pattern = r'^[!@#$%^&*()_+{}\[\]:;<>,.?/\\|]+$'
		regex =r'^[a-zA-Z]+$' 
		pattern1 =   r'^[+-]?\d*\.?\d+$'
 
		if amount == "":
			messagebox.showerror("Error !!", "Amount is empty,\nPlease enter valid amount")
		elif amount.isspace():
			messagebox.showerror("Error !!", "Amount should not contain spaces")
			ent_amt.delete(0, tk.END)
			ent_amt.focus_set()
		elif re.search(pattern, amount):
			messagebox.showerror("Error !!", "Amount should not contain special characters")
			ent_amt.delete(0, tk.END)
			ent_amt.focus_set()
		elif re.search(regex,  amount):
			messagebox.showerror("Error !!", "Amount should not contain alphabets")
			ent_amt.delete(0, tk.END)
			ent_amt.focus_set()
		elif not re.search(pattern1,  amount):
			messagebox.showerror("Error !!", "Amount should not contain combination of digits, alphabets or special characters")
			ent_amt.delete(0, tk.END)
			ent_amt.focus_set()
		else:
			amount = float(amount)
			if ((amount == 0.0) or (amount > 10000)):
				messagebox.showerror("Error !!", "Amount should be between 1 to 10000. ")
				ent_amt.delete(0, tk.END)
				ent_amt.focus_set()
			elif amount < 0.0:
				messagebox.showerror("Error !!", "Amount should be greater than 0")
				ent_amt.delete(0, tk.END)
				ent_amt.focus_set()
			else:
				url = 'https://api.exchangerate-api.com/v4/latest/' + from_currency.upper()
				res = get(url)
				# print(res)
				data = res.json()
				# print(data)
				from_rate = data["rates"][from_currency.upper()]
				# print(from_rate)
				to_rate = data["rates"][to_currency.upper()]
				# print(to_rate)
				converted_amt = amount * (to_rate / from_rate)
				# print("ca", converted_amt)
				new_amt =  f"{converted_amt:.3f} " + to_currency
				ans_box.config(text = new_amt)
	except Exception as e:
		messagebox.showerror("Error", e)	

#Convert Button 
convert_btn = Button(root, text = "Convert", font = f1, bg = "orange", relief = "solid", command=convert)
convert_btn.place(x=120, y = 250)

def clear_fields():
	ent_amt.delete(0, tk.END)
	combo1.set(default_value1)
	combo2.set(default_value2)
	ans_box.config(text = "")

#Clear Button
clear_btn = Button(root, text = "Reset", font = f1, bg = "violet", relief = "solid", command=clear_fields)
clear_btn.place(x=300, y = 250)

#Converted Amount
ans_box = Label(root, text = " ",width = 18,height= 2, pady =10,relief = "solid", anchor=CENTER, font=("Helvetica 18 bold") , bg = "white", fg = "black")
ans_box.place(x=120, y=320)

root.mainloop()
