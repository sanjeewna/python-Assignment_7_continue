class AirportData:
    def __init__(self):
        self.airports = {}

    def add_airport(self, icao, name):
        self.airports[icao] = name

    def fetch_airport_info(self, icao):
        return self.airports.get(icao, "Airport not found")

def main():
    airport_db = AirportData()

    while True:
        print("\nAirport Data")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            icao = input("Enter the ICAO code of the airport: ")
            name = input("Enter the name of the airport: ")
            airport_db.add_airport(icao, name)
            print("Airport added successfully!")

        elif choice == '2':
            icao = input("Enter the ICAO code of the airport: ")
            info = airport_db.fetch_airport_info(icao)
            print(f"Name of the airport: {info}")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
