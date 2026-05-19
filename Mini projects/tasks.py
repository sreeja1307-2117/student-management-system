
print("task1")

data = {}
data["name"]= input("Enter your name: ")
data["age"]= input("Enter your age: ")
data["city"]= input("Enter your city: ")
data["country"]= input("Enter your country: ") 

print(data)
print("task2")

contacts = {}
for i in range(3):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
print(contacts)

