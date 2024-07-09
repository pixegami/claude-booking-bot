import csv
from datetime import datetime, timedelta


def get_booking_slots(party_size: int, time: str):
    # Read the CSV file
    with open("data/bookings.csv", "r") as file:
        reader = csv.DictReader(file)
        bookings = list(reader)

    # Convert input time to datetime object
    input_time = datetime.strptime(time, "%H:%M")

    # Define the time range (1 hour before and after the input time)
    time_range_start = input_time - timedelta(hours=1)
    time_range_end = input_time + timedelta(hours=1)

    # Find available slots
    available_slots = []
    for booking in bookings:
        booking_time = datetime.strptime(booking["time"], "%H:%M")

        # Check if the booking time is within the 1-hour range
        if time_range_start <= booking_time <= time_range_end:
            for table, value in booking.items():
                if table != "time":
                    table_size = int(table.split("(")[1].split("p")[0])
                    if table_size >= party_size and value == "":
                        available_slots.append(
                            {
                                "party_size": party_size,
                                "time": booking["time"],
                                "table": table,
                            }
                        )

    # Sort the available slots by time
    available_slots.sort(key=lambda x: x["time"])
    results_list = []
    for slot in available_slots:
        results_list.append(f"🕒 {slot['time']} - {slot['table']}")

    result_string = str(results_list)
    return result_string


# Example usage
if __name__ == "__main__":
    print(get_booking_slots(4, "19:14"))
