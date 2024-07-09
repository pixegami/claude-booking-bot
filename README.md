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

