class Flight:
    def __init__(self, flight_number, origin, destination, seat_capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.seat_capacity = seat_capacity
        self.available_seats = seat_capacity
        self.bookings = {}

    def book_seat(self, passenger_name, seat_number):
        if self.available_seats <= 0:
            print("Sorry, this flight is fully booked.")
            return False
            
        if seat_number in self.bookings:
            print(f"Seat {seat_number} is already taken.")
            return False
            
        self.bookings[seat_number] = passenger_name
        self.available_seats -= 1
        print(f"Booking confirmed! {passenger_name} has seat {seat_number}.")
        return True

    def cancel_booking(self, seat_number):
        if seat_number not in self.bookings:
            print(f"No booking found for seat {seat_number}")
            return False
            
        passenger_name = self.bookings[seat_number]
        del self.bookings[seat_number]
        self.available_seats += 1
        print(f"Cancellation successful! Seat {seat_number} is now available.")
        return True

    def show_flight_details(self):
        print(f"\nFlight {self.flight_number}:")
        print(f"Route: {self.origin} -> {self.destination}")
        print(f"Seats: {self.available_seats}/{self.seat_capacity} available")
        if self.bookings:
            print("\nCurrent Bookings:")
            for seat, name in self.bookings.items():
                print(f"Seat {seat}: {name}")


class FlightSystem:
    def __init__(self):
        self.flights = {}
        self.users = {}
        self.current_user = None

    def add_flight(self):
        print("\nAdd New Flight")
        flight_number = input("Enter flight number: ").strip().upper()
        if flight_number in self.flights:
            print("Flight number already exists!")
            return
            
        origin = input("Origin: ").strip().title()
        destination = input("Destination: ").strip().title()
        
        while True:
            try:
                capacity = int(input("Seat capacity: "))
                break
            except ValueError:
                print("Please enter a valid number")
                
        self.flights[flight_number] = Flight(flight_number, origin, destination, capacity)
        print(f"\nFlight {flight_number} added successfully!")

    def book_seat(self):
        if not self.flights:
            print("No flights available. Please add flights first.")
            return
            
        self.show_flights()
        flight_number = input("\nEnter flight number to book: ").strip().upper()
        
        if flight_number not in self.flights:
            print("Flight not found!")
            return
            
        flight = self.flights[flight_number]
        passenger_name = input("Passenger name: ").strip()
        
        print("\nAvailable seats:", ", ".join(
            str(seat) for seat in range(1, flight.seat_capacity + 1) 
            if str(seat) not in flight.bookings
        ))
        
        seat_number = input("Seat number: ").strip()
        flight.book_seat(passenger_name, seat_number)

    def cancel_booking(self):
        if not self.flights:
            print("No flights available.")
            return
            
        self.show_flights()
        flight_number = input("\nEnter flight number: ").strip().upper()
        
        if flight_number not in self.flights:
            print("Flight not found!")
            return
            
        flight = self.flights[flight_number]
        
        if not flight.bookings:
            print("No bookings for this flight.")
            return
            
        seat_number = input("Enter seat number to cancel: ").strip()
        flight.cancel_booking(seat_number)

    def show_flights(self):
        if not self.flights:
            print("No flights available.")
            return
            
        print("\nAvailable Flights:")
        for flight in self.flights.values():
            flight.show_flight_details()

    def register_user(self):
        print("\nUser Registration")
        username = input("Choose a username: ").strip()
        
        if username in self.users:
            print("Username already exists!")
            return
            
        password = input("Choose a password: ").strip()
        self.users[username] = password
        print("Registration successful!")

    def login(self):
        print("\nUser Login")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"\nWelcome, {username}!")
            return True
        else:
            print("Invalid username or password")
            return False

    def logout(self):
        self.current_user = None
        print("Logged out successfully.")

    def run(self):
        while True:
            print("\n==== Flight Booking System ====")
            if self.current_user:
                print(f"Logged in as: {self.current_user}")
                print("1. Add Flight")
                print("2. Book a Seat")
                print("3. Cancel Booking")
                print("4. Show Flights")
                print("5. Logout")
                print("6. Exit")
            else:
                print("1. Login")
                print("2. Register")
                print("3. Show Flights")
                print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if not self.current_user:
                if choice == "1":
                    if self.login():
                        continue
                elif choice == "2":
                    self.register_user()
                elif choice == "3":
                    self.show_flights()
                elif choice == "4":
                    print("Thank you for using the Flight Booking System!")
                    break
                else:
                    print("Invalid choice")
            else:
                if choice == "1":
                    self.add_flight()
                elif choice == "2":
                    self.book_seat()
                elif choice == "3":
                    self.cancel_booking()
                elif choice == "4":
                    self.show_flights()
                elif choice == "5":
                    self.logout()
                elif choice == "6":
                    print("Thank you for using the Flight Booking System!")
                    break
                else:
                    print("Invalid choice")


if __name__ == "__main__":
    system = FlightSystem()
    system.run()
