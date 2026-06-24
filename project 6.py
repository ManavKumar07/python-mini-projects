#PROJECT 6
#contact book - Add search, update, delete contact in a dictonary. Uses sets to detect duplicate numbers
contacts={}
numbers= set()
while True:   
    print("Enter your choice what do you want to do:--")
    print("1.Add conatct")
    print("2.Search contact")
    print("3.Update conatct")
    print("4.delete contact")
    ch=int(input("Enter your choice:--"))
    if (ch==1):
        name = input("Enter name: ")
        num = input("Enter number: ")
        print("Number added!")    
        if num in numbers:
            print("Duplicate number found")
        else:
            contacts[name]=[num]
            numbers.add(num)
    elif(ch==2):
        name = input("Enter name to search: ")
        print("Number:", contacts.get(name, "Not found"))
        print("Number fetched sucessfuly!!")
    elif ch == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            num = input("Enter new number: ")
            contacts[name] = num
        else:
            print("Contact not found")
    elif ch == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            numbers.remove(contacts[name])
            del contacts[name]
    elif ch == 5:
        break
print("Thanks for using!")