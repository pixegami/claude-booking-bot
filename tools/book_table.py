import csv
from datetime import datetime


def book_table(table_name: str, time: str, reservation_name: str) -> bool:
    # Convert input time to datetime object for comparison
    input_time = datetime.strptime(time, "%H:%M")

    # Read the current bookings
    with open("data/bookings.csv", "r") as file:
        reader = csv.DictReader(file)
        bookings = list(reader)

    # Find the correct row and check if the slot is available
    for booking in bookings:
        booking_time = datetime.strptime(booking["time"], "%H:%M")
        if booking_time == input_time and table_name in booking:
            if booking[table_name] == "":
                # The slot is available, update it
                booking[table_name] = reservation_name

                # Write the updated bookings back to the CSV
                with open("data/bookings.csv", "w", newline="") as file:
                    fieldnames = reader.fieldnames
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(bookings)

                return (
                    f"✅ Booking Success: {table_name} at {time} for {reservation_name}"
                )
            else:
                return f"❌ Booking Failed: {table_name} at {time} is already booked"

    return f"❌ Booking Failed: {table_name} at {time} not found"
