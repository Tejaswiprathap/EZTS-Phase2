'''retrieve data from set of info. such as retrieving A's age/name/id,etc...'''
names = []
ages = []
emails = []
gender=[]

ppls= int(input("Enter the number of people: "))
for i in range(ppls):
    print(f"\nEnter details for person {i+1}:")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email ID: ")
    gen=input("Gender: ")

    names.append(name)
    ages.append(age)
    emails.append(email)
    gender.append(gen)
def print_attribute(name, attribute):
    index = names.index(name)
    if attribute == "age":
        print(f"{name}'s age is {ages[index]}")
    elif attribute == "email":
        print(f"{name}'s email is {emails[index]}")
    elif attribute=="gen":
        print(f"{name}'s gender is {gender[index]}")
    else:
        print("Invalid attribute!")
search_name = input("\nEnter the name of the person to search for: ")
search_attribute = input("Enter the attribute (age/email/gender) to retrieve: ")

if search_name in names:
    print_attribute(search_name, search_attribute)
else:
    print("Person not found!")
