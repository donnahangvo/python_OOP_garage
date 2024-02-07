# ''' Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# By the end of this project each student should be able to:
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation
#     '''

class ParkingGarage:

    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parking_spaces = list(range(1, total_parking_spaces + 1))
        self.current_ticket = None

    # Take Ticket Method
        
    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            space = self.parking_spaces.pop(0)
            self.current_ticket = {"ticket_number": ticket, "parking_space": space, "paid": False}
            print(f"Ticket {ticket} issued. Parking space {space} allocated.")
        else:
            print("Sorry, the parking lot is full. No more tickets available.")

    # Pay For Parking Method

    def payForParking(self):
        if self.current_ticket:
            amount_paid = input("Enter 'paid' to pay for parking: ")
            if amount_paid:
                self.current_ticket["paid"] = True
                print("Ticket paid. You have 15 minutes to leave.")
            else:
                print("Payment not received.")
        else:
            print("No active ticket. Please take a ticket first.")

    # Leave Garage Method

    def leaveGarage(self):
        if self.current_ticket:
            if self.current_ticket["paid"]:
                print("Thank You, have a nice day!")
            else:
                payment = input("Payment pending. Enter payment: ")
                if payment:
                    print("Thank you, have a nice day!")
                    self.tickets.append(self.current_ticket["ticket_number"])
                    self.parking_spaces.append(self.current_ticket["parking_space"])
                else:
                    print("Payment not received. Please pay to exit.")
            self.current_ticket = None
        else:
            print("No active ticket. Please take a ticket first.")

# Instantiating ParkingGarage class

def garage_test():
    garage = ParkingGarage(total_tickets=10, total_parking_spaces=10)

    while True:
        print("\nOptions:")
        print("1. Take Ticket")
        print("2. Pay for Parking")
        print("3. Leave Garage")
        print("4. Quit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            garage.takeTicket()
        elif choice == "2":
            garage.payForParking()
        elif choice == "3":
            garage.leaveGarage()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter an option between 1 and 4.")

garage_test()






# Please Ignore The Code Below

# class Garage():

#     def __init__(self, ticket, space, currentTicket):
#         self.ticket = ticket
#         self.space = space
#         self.currentTicket = currentTicket

#         self.ticket = []
#         self.space = []
#         self.currentTicket = {}


#     # Method to takeTicket, decrease amount of tickets and spaces


#     def takeTicket(self):

#         self.ticket = input('ticket')
#         self.space = input('space')
#         self.currentTicket[self.ticket]= self.space  

#     # Method to show available parking spaces

#     # def showCapacity(self):
#     #     if self.space > 0:
#     #         print(f'There are currently {self.space} spaces available.')

#     #     else:
#     #         print("There are no available spaces.")

#     # Method to payForParking


#     def payForParking(self):

#         while False:
#             park_pay = input('How long did you park?')
#             total_park = {self.time(park_pay)} * 3
#             print(f'Your total is {total_park} ')
#             pay_amount = input(f'Would you like to pay? yes/no')
#             if pay_amount == 'yes':
#                 return True


#     # Instantiating methods for Garage


# Parking = Garage('current_ticket', 'ticket', 'space')

# def park():
    
#     while True:
#         response = input('Welcome to THE GARAGE, what would you like to do? new/leave')

#         # new = new customer
#         # leave = pay for parking and then leave

#         if response.lower() == 'new':
#             Parking.takeTicket()
#             # print(Parking.showCapacity)
        
#         # elif response.lower() == 'leave':
#         #     Parking.payForParking()
        
#         else:
#             break

# # def pay():

# #     while True:
# #         response = input('Would you like to leave THE GARAGE? yes/no')

# #         if response.lower() == '':
# #             print('Thank you have a nice day!')

# #         elif response.ceil() >= 1:
# #             print('Your total is {}')
