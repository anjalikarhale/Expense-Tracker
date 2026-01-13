from datetime import datetime
class Expense:
    def __init__(self, category, amount):
        self.date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.category = category
        self.amount = amount
       
    def show_details(self):
        print("Date and Time: ", self.date_time)
        print("Category: ",self.category)
        print("Amount: ", self.amount)
   
expenses = []
try:
    file = open("expense.txt","r")
    for line in file:
        category,amount,date_time = line.strip().split(",")
        expense = Expense(category, int(amount))
        expense.date_time = date_time
        expenses.append(expense)
    file.close()
except FileNotFoundError:
    print("No previous data found, starting fresh")
while True:
    print("------MENU------")
    print("1.Add Expenses")
    print("2.View all expenses")
    print("3.Search by category")
    print("4.Total expenses")
    print("5.Date-wise filter")
    print("6.Monthly report")
    print("7.Delete expense")
    print("8.Update expense")
    print("9.Exit")
    choice = int(input("Enter your choice: "))
   
    if choice==1:
        category = input("Enter category: ")
        amount = int(input("Enter amount: "))
       
        expense = Expense(category, amount)
        expenses.append(expense)
        print("Added successfully!")
       
    elif choice==2:
        if not expenses:
            print("No expense added")
        else:
            for expense in expenses:
                print("")
                expense.show_details()
                print("")
   
    elif choice==3:
        category = input("Enter category: ")
        found = False
        for expense in expenses:
            if expense.category.lower()==category.lower():
                print("")
                expense.show_details()
                print("")
                found = True
           
        if not found:
            print("Category not found")
           
    elif choice==4:
        total_expense = 0
        for expense in expenses:
            total_expense = total_expense+ expense.amount
        print("Total expense = ", total_expense)
       
    elif choice==5:
        date_time = input("Enter date: ")
        found = False
        for expense in expenses:
            if expense.date_time[:10]==date_time:
                expense.show_details()
                found = True
        if not found:
            print("No expense of this date found")
   
    elif choice==6:
        month = input("Enter month and year(mm-yyyy): ")
        found=False
        for expense in expenses:
            if expense.date_time[3:10] == month:
                expense.show_details()
                found=True
        if not found:
            print("No expense found in this month")
               
    elif choice==7:
        if not expenses:
            print("Not found")
        else:
            print("Expense list")
            for i, expense in enumerate(expenses, start=1):
              print(i,expense.category, expense.amount)
            delete = int(input("Enter which expense to delete: "))
            index = delete-1
       
            if index>=0 and index <len(expenses):
              expenses.pop(index)
              print("Deleted succesfully!")
            else:
              print("Invalid input")

           
    elif choice==8:
        if not expenses:
            print("not found")
        else:
            print("Expense list")
            for i, expense in enumerate(expenses, start=1):
                print(i, expense.category,expense.amount)
        update = int(input("Enter the choice you want to update: "))
        index = update-1
       
        if index>=0 and index<len(expenses):
            print("1.Update category")
            print("2.Update amount")
            next_update = int(input("Enter your choice: "))
           
            if next_update==1:
                expenses[index].category = input("Enter category: ")
                print("Updated successfully!")
            elif next_update==2:
                expenses[index].amount = int(input("Enter the amount: "))
                print("Updated successfully!")
            else:
                print("Invalid choice")
               
    elif choice==9:
        file = open("expense.txt","w")
        for expense in expenses:
          file.write(f"{expense.category},{expense.amount},{expense.date_time}\n")
        file.close()
        print("Data Saved")
        break
       
    else:
        print("Invalid choice")


