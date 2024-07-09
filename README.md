# Claude Tools Project: Booking Bot

This is an example project to show you how to use Claude 3.5's "tool use" functionality. Tools are custom functions that we can tell Claude about, and then Claude can decide to "use" them by sending us the intent and input as its response.

The project will be a Claude chat bot that helps us check and reserve tables at a restaurant (data stored as a CSV file on disk).

## Setting Up

I normally like to use a virtual environment in Python to set up my dependencies.

```sh
# Create a virtual environment named "venv".
python -m venv venv

# Active the environment (on Mac or Linux — other shells may differ).
source venv/bin/activate
```

Install dependencies (frozen to this project's version — but you can try using latest if you want).

```sh
pip install -r requirements.txt
```

You will also need an API key from https://console.anthropic.com/. Go there to set up an account, upgrade to "builder" plan, add credits, then get an API key. Then add it to your environment variable.

```sh
export ANTHROPIC_API_KEY="your_api_key_here"
```

## Data Source

The data source is a CSV file on disk at `data/bookings.csv`. The bot will have access to this file, and will be able to modify it.

The data shows which tables / times are available (if free), or the name of whoever has booked that slot.

Here's an example of the data.

Here's the table expressed as markdown, truncated to 4 columns and 4 rows:

| time  | table1 (2p) | table2 (2p) | table3 (2p) |
| ----- | ----------- | ----------- | ----------- |
| 12:00 |             | Jones       |             |
| 12:30 | Anderson    | Liam H      | Jackson K   |
| 13:00 | Li          | Patel       | Johnson     |
| 13:30 | Martin      |             |             |

## Available Tools

The tools will be implemented as separate Python functions. We will have three tools.

```python
def ask_user(input_prompt: str) -> str:
    # Show an input prompt so the user can chat / enter information.
```

```python
def get_booking_slots(party_size: int, time: str):
    # Which tables (of "party size") are free near the desired time (e.g. 9:30)?
```

```python
def book_table(table_name: str, time: str, reservation_name: str) -> bool:
    # Show an input prompt so the user can chat / enter information.
```

## Booking Bot Implementation

The actual bot (using the tool) is implemented in `booking_bot.py`. It is structured to continue prompting and responding to the user in a loop (until the booking is made, or cancelled).

It can be used like this:

```sh
python booking_bot.py
```

Example output and conversation flow:

```
💬 Tell me about the time/seats you'd like to book.
👉 Enter Message: Any tables available at 7pm?
✨ System Response: Certainly! I'd be happy to help you check for available tables at 7 PM. However, to provide you with accurate information, I'll need to know how many people will be in your party. This information is essential for finding a suitable table. Let me ask you for that detail.

💬 How many people will be in your party for the 7 PM reservation?
👉 Enter Message: 2
🛠️ Using Tool [ask_user]: 2

✨ System Response: Thank you for providing that information. Now I can check for available tables at 7 PM for a party of 2. Let me search for you.

🛠️ Using Tool [get_booking_slots]: ['🕒 18:00 - table3 (2p)', '🕒 19:30 - table2 (2p)', '🕒 20:00 - table1 (2p)', '🕒 20:00 - table2 (2p)', '🕒 20:00 - table4 (2p)', '🕒 20:00 - table7 (4p)']

✨ System Response: I've checked the available booking slots for a party of 2 around 7 PM. Unfortunately, there isn't a table available exactly at 7 PM, but I can offer you some alternatives:

1. Earlier option:
   - 6:00 PM (18:00) - table3 (2-person table)

2. Later options:
   - 7:30 PM (19:30) - table2 (2-person table)
   - 8:00 PM (20:00) - multiple tables available (table1, table2, table4 - all 2-person tables)

Would you like to book one of these available times, or would you prefer to check for a different time or party size?

💬 Please let me know if you'd like to book one of these times or if you'd like to explore other options.
👉 Enter Message: Let's book something at 6pm.
🛠️ Using Tool [ask_user]: Let's book something at 6pm.

✨ System Response: Excellent choice! I'm happy to help you book a table for 6:00 PM (18:00). To confirm, we have a table for 2 people available at that time. Before I make the reservation, I just need one more piece of information from you.

💬 Under what name would you like to make the reservation?
👉 Enter Message: Jack
🛠️ Using Tool [ask_user]: Jack

✨ System Response: Thank you, Jack. I'll go ahead and book the table for you now.

🛠️ Using Tool [book_table]: ✅ Booking Success: table3 (2p) at 18:00 for Jack

✨ System Response: Great news, Jack! Your reservation has been successfully booked. Here are the details of your reservation:

- Name: Jack
- Table: table3 (2-person table)
- Date: Today
- Time: 6:00 PM (18:00)
```
