class SimpleModel:
    def __init__(self):
        self.data = []
    
    def add_data(self):
        value = input("Enter something : ")
        self.data.append(value)
        print(f"{value} Added to the list...")
    def view_data(self):
        print("Here's what you entered...")
        for item in self.data:
            print(item)

def main():
    model = SimpleModel()
    while True:
        print("\n1. Add Something")
        print("2. View Data")
        print("3. Exit")
        choice = input("What do you want to do? : ")
        if choice == "1":
            model.add_data()
        elif choice == "2":
            model.view_data()
        elif choice == "3":
            print("Program Finish...")
            break
        else:
            print("Invalid Choice try again...")

main()