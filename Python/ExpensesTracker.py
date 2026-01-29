import os
import json

try:
    with open('expenses_tracker.json','r')as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

is_recording = True

while is_recording :
        amount = int(input("How Much did you Spent THIS time:  "))
        category = input("Why Did you Spent? Category:  ")
        notes = input("Some Notes: ")
        
        more_expenses = input("More Expenses? Yes Or No:  ").strip().lower()
        
        if more_expenses == "no": 
              is_recording = False
        elif more_expenses =='yes':
              print('OK Keep Going')
        else:
              print('Ummm Yes or No, We havent Added Your Previous Expense Add it Again')
              continue
        expenses.append({"amount":amount,"category":category,"comments":notes})
        

print(f"While we are Updating it Here is an Overview of it => {expenses}")
with open('expenses_tracker.json','w') as file:
        json.dump(expenses,file,indent=2)
# Only Yes and No for scaling purposes 

