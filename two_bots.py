# two_bots.py
# Author: Isabella Meyer

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

orders = {"A100": "shipped"}
stock = {"rain jacket": 12}

order_tool = OrderLookup(orders)
stock_tool = StockLookup(stock)

sunny = SupportChatbot(
    "Sunny",
    "You are cheerful and brief.",
    order_tool,
    stock_tool,
)

river = SupportChatbot(
    "River",
    "You are formal and detailed.",
    order_tool,
    stock_tool,
)

sunny_first_reply = sunny.respond("hello")
sunny.respond("Where is order A100?")

river_first_reply = river.respond("hello")

print(sunny.name, len(sunny.history))
print(river.name, len(river.history))
print(sunny_first_reply)
print(river_first_reply)
print(sunny.instructions)
print(river.instructions)
