import time

emergency_contacts = []

def add_contact(name, phone):
    emergency_contacts.append({"name": name, "phone": phone})
    print(f"Contact added: {name} - {phone}")

def show_contacts():
    print("\nEmergency Contacts:")
    for c in emergency_contacts:
        print(f"{c['name']} - {c['phone']}")
def send_sos(location):
    if not emergency_contacts:
        print("No emergency contacts saved!")
        return
    
    print("\n🚨 SOS Alert Sent 🚨")
    for c in emergency_contacts:
        print(f"Alert sent to {c['name']} ({c['phone']}) with location: {location}")
        time.sleep(1)

print("Women Safety & Location Alert App")

while True:
    print("\n1. Add Emergency Contact\n2. View Contacts\n3. Send SOS\n4. Exit")
    choice = input("Choose option: ")
    if choice=="1":
        name=input("Enter name:")
        phone=input("Enter phone:")
        add_contact(name,phone)
    elif choice=="2":
        show_contacts()
    elif choice=="3":
        location=input("Enter current location/coordinates:")
        send_sos(location)
    elif choice=="4":
        break
    else:
        print("Invalid option")    
