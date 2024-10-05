import json
from anthropic.types.tool_use_block import ToolUseBlock

from tools.ask_user import ask_user
from tools.book_table import book_table
from tools.get_booking_slots import get_booking_slots


def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as file:
        schema = json.load(file)
    return schema


# Load each of the tool schemas.
ask_user_schema = load_schema("tools/schema/ask_user.json")
get_booking_slots_schema = load_schema("tools/schema/get_booking_slots.json")
book_table_schema = load_schema("tools/schema/book_table.json")


def use_tool(tool_use_content: ToolUseBlock) -> dict:
    """Helper function to use the correct tool based on the tool_use_content."""

    print(f"Tool use Block: {tool_use_content}")

    tools_map = {
        "ask_user": ask_user,
        "get_booking_slots": get_booking_slots,
        "book_table": book_table,
    }

    tool_name = tool_use_content.name
    tool_input = tool_use_content.input
    tool_function = tools_map[tool_name]

    return tool_function(**tool_input)
