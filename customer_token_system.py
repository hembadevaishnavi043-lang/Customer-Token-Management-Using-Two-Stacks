
# Customer Service Token Management System
# Queue Implementation Using Two Stacks

class CustomerQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.token_number = 1

    # Add customer to queue
    def add_customer(self, name):
        customer = {
            "token": self.token_number,
            "name": name
        }

        self.stack1.append(customer)
        print("Customer added successfully!")
        print("Token Number:", self.token_number)
        print("Customer Name:", name)

        self.token_number += 1

    # Move customers from stack1 to stack2
    def transfer_stack(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    # Serve next customer
    def serve_customer(self):
        if not self.stack2:
            self.transfer_stack()

        if not self.stack2:
            print("No customers waiting!")
            return

        customer = self.stack2.pop()

        print("\nServing Customer")
        print("Token Number:", customer["token"])
        print("Customer Name:", customer["name"])

    # Display waiting queue
    def display_queue(self):
        waiting = self.stack2[::-1] + self.stack1

        if not waiting:
            print("Queue is empty!")
            return

        print("\n----- Waiting Customers -----")

        for customer in waiting:
            print(
                "Token:", customer["token"],
                "| Name:", customer["name"]
            )

    # Count waiting customers
    def count_customers(self):
        total = len(self.stack1) + len(self.stack2)
        print("Total Waiting Customers:", total)


# Main program
queue = CustomerQueue()

while True:
    print("\n===== Customer Token Management =====")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Waiting Queue")
    print("4. Count Waiting Customers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ").strip()

        if name:
            queue.add_customer(name)
        else:
            print("Customer name cannot be empty!")

    elif choice == "2":
        queue.serve_customer()

    elif choice == "3":
        queue.display_queue()

    elif choice == "4":
        queue.count_customers()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
