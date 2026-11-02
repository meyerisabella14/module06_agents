# my_main.py
# Author: Isabella Meyer

from my_assistant import PilatesAssistant
from my_tool import ClassSchedule

SCHEDULE = {
    "monday": ["8:00 am", "5:30 pm"],
    "wednesday": ["9:00 am", "6:00 pm"],
    "friday": ["7:30 am", "10:00 am"],
}

schedule_tool = ClassSchedule(SCHEDULE)
bot = PilatesAssistant("Bella", schedule_tool)

print("Welcome to the Pilates Studio!")
print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
