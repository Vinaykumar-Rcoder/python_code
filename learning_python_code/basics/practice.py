
# User se number lo, agar 50 se bada ho to "Too high", chhota ho to "Too low", aur barabar ho to "Correct" print karo.


add_number = int(input("Enter a number :"))
if add_number > 50:
    print("Too high")
elif add_number < 50:
    print("Too low")
else:
    print("correct")

#write a function for check even aur odd.

number = int(input("Enter a number : "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# categorize a person as Teen, Adult, or Senior based on their age.

age = int(input("Enter age : "))
if age < 13:
    print("child")
elif 12 < age <= 19:
    print("Teen")
elif 19 < age <= 60:
    print("Adult")
else :
    print("senior")
# check user name aur password
username = input("Enter a username :")
password =(input("Enter a password :"))

if username == "Thakur":
     if password == "01234":
         print("login success")
     else:
         print("password not ok")
else:
    print("user not ok")
# calculator program
Number_1 = int(input("Enter number first : "))
operator = input("Enter operator :")
Number_2 = int(input("Enter number second : "))


if operator == "+":
    print(Number_1 + Number_2)
elif operator == "-":
    print(Number_1 - Number_2)
elif operator == "*":
    print(Number_1 * Number_2)
elif operator == "/":
    print(Number_1 / Number_2)
else:
    print("No Answer")

#******** ATM service 

balance = 2000

print("1. check balance ")
print("2. withdraw ")
print("3. Deposit ")

choice = int(input("Enter your choice : ")) 

if choice == 1:
    print("Your current balance is : ", balance)

elif choice == 2:
     amount = float(input("Enter withdraw amount :"))
     if amount > balance:
        print("insufficient balance")
     else:
         balance-=amount
         print(" Withdraw successful")
         print("Your remaining balance is :",balance)
elif choice == 3:
    amount = float(input("Enter Deposit amount :"))
    balance +=amount
    print("Deposit successful")
    print("Your current balance is :",balance)

else:
    print("Invalid choice")



print (" Welcome to india mart ")

amount = int(input("Enter total amount: "))

if amount >= 5000:
    discount = amount * 0.20

elif amount >= 2000:
    discount = amount * 0.10

else:
    print("No discount")

final_amount = amount - discount

print("Discount :",discount)
print("Final Amount to Pay :", final_amount)

# , Yellow, Red , Green signal color with instractions 

user = input(" Enter color: ")

if user == "red":
    print("stop")
elif user == "yellow":
    Print("Ready")
elif user == "green":
    print("Go")
else:
    print("Ivalid")

