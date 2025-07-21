import mysql.connector as c
con = c.connect(host = "localhost", user = "root", passwd = "Arpan@2003#1984", database = "project")

cursor = con.cursor()
print("*" * 65)
print(" " * 25, end = 'Bank management system')
print("*"*65)
accno = 100
while True:
    choice = int(input("1-> OPEN ACCOUNT\n2-> CASH WITHDRAWL\n3-> CASH DEPOSITE\n4-> ACCOUNT STATEMENT\n5-> UPDATE ACCOUNT\n6-> EXIT\n...ENTER YOUR CHOICE: "))
    if choice == 1:
        name = input("Enter name of Account holder: ")
        balance = int(input("Enter opening balance: "))
        mobile = input("Enter Registered Mobile Number: ")

        cursor.execute("SELECT MAX(accno) FROM bank")
        last_acc = cursor.fetchone()[0]
        accno = last_acc + 1 if last_acc is not None else 101

        accno += 1
        query = "Insert into BANK values({},'{}',{},'{}')".format( accno,name, balance, mobile)
        cursor.execute(query)
        con.commit()
        print("Account opened successfully.")


    elif choice == 2:
        accno = int(input("Enter Account Number to withdraw money: "))
        name = input("Enter name of Account holder: ")

        query = "select * from bank WHERE accno = %s AND name = %s"
        cursor.execute(query, (accno, name))
        data = cursor.fetchone()

        if data:
            current_balance = data[2]
            withdrawal_amount = int(input("Enter withdrawal amount: "))

            if withdrawal_amount > current_balance:
                print("Insufficient balance.")
            else:
                new_balance = current_balance - withdrawal_amount
                update_query = "UPDATE bank SET balance = %s WHERE accno = %s"
                cursor.execute(update_query, (new_balance, accno))
                con.commit()
                print(f"Withdrawal successful. Remaining balance: {new_balance}")
        else:
            print("Account not found.")



    elif choice == 3:
        accno = int(input("Enter Account Number to deposit money: "))
        name = input("Enter name of Account holder: ")

        query = "SELECT * FROM bank WHERE accno = %s AND name = %s"
        cursor.execute(query, (accno, name))
        data = cursor.fetchone()

        if data:
            current_balance = data[2]
            deposite_amount = int(input("Enter deposite amount: "))
            new_balance = current_balance + deposite_amount
            update_query = "UPDATE bank SET balance = %s WHERE accno = %s"
            cursor.execute(update_query, (new_balance, accno))
            con.commit()
            print(f"Deposite successful. Current balance: {new_balance}")
        else:
            print("Account not found.")

    elif choice == 4:
        accno = int(input("Enter Account Number to view Account Details: "))
        name = input("Enter name of Account holder: ")
        query = "SELECT * FROM bank WHERE accno = %s AND name = %s"
        cursor.execute(query, (accno, name))
        data = cursor.fetchone()
        if data:
            print("Account Details:")
            print(f"Account Number: {data[0]}\nAccount Name: {data[1]}\nAccount Balance: {data[2]}\nRegistered Mobile number: {data[3]}\n")
        else:
            print("Account not found.")

    elif(choice == 5):
        accno = int(input("Enter Account Number to update your Account Details: "))
        name = input("Enter current name of Account holder: ")

        query = "SELECT * FROM bank WHERE accno = %s AND name = %s"
        cursor.execute(query, (accno, name))
        data = cursor.fetchone()
        if data:
            update_details = input("Which detail do you want to update?\n1. Name\n2. Mobile no.\n")

            if update_details == "1":
                update_name = input("Enter new Account holder Name: ")
                query = "UPDATE bank SET name = %s WHERE accno = %s"
                cursor.execute(query, (update_name, accno))
                con.commit()
            elif update_details == "2":
                update_mobile = input("Enter new Mobile Number: ")
                query = "UPDATE bank SET mob = %s WHERE accno = %s"
                cursor.execute(query, (update_mobile, accno))
                con.commit()
            print("Account updated successfully.")
        else:
            print("Account not found.")
    elif choice == 6:
        print("Exiting... Thank you for using the Bank Management System!")
        con.close()
        break
    else:
        print("Invalid choice.Please try again.")
    print("Thank you! Visit Again...")
