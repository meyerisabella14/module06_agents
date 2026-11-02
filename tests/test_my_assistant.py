from my_assistant import PilatesAssistant
from my_tool import ClassSchedule


def make_assistant():
    schedule = {
        "monday": ["8:00 am", "5:30 pm"],
        "friday": ["7:30 am", "10:00 am"],
    }
    tool = ClassSchedule(schedule)
    return PilatesAssistant("Bella", tool)


def test_schedule_lookup():
    bot = make_assistant()
    reply = bot.respond("What classes are available Monday?")
    assert "8:00 am" in reply


def test_unknown_day():
    bot = make_assistant()
    reply = bot.respond("What classes are available Tuesday?")
    assert "Which day" in reply


def test_booking_goes_to_front_desk():
    bot = make_assistant()
    reply = bot.respond("Can I book a class?")
    assert "front desk" in reply


def test_history_records_messages():
    bot = make_assistant()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
