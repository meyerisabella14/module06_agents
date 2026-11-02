# my_assistant.py
# Author: Isabella Meyer


class PilatesAssistant:
    """A mock assistant that answers Pilates schedule questions."""

    def __init__(self, name, schedule_tool):
        # Store the assistant's name and schedule tool.
        self.name = name
        self.schedule_tool = schedule_tool

        # Keep a separate conversation history for this assistant.
        self.history = []

    def respond(self, user_message):
        # Record the customer's message.
        self.history.append({"role": "user", "content": user_message})

        # Choose a response using simple rules.
        reply = self.choose_reply(user_message)

        # Save the assistant's reply.
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        # Lowercase the message so matching is easier.
        text = user_message.lower()

        # Booking requests must be handled by a person.
        if "book" in text or "cancel" in text:
            return "I can't change bookings. Please contact the front desk."

        # Answer questions about class availability.
        if "class" in text or "available" in text or "schedule" in text:
            day = self.schedule_tool.find_day(text)

            # Ask for a day when no matching day is found.
            if day is None:
                return "Which day? I can check Monday, Wednesday, or Friday."

            times = self.schedule_tool.times_for(day)
            return f"Pilates classes on {day}: {', '.join(times)}."

        # Respond to greetings.
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can check Pilates class times."

        # Safely handle requests outside this assistant's abilities.
        return "I'm not sure how to help with that. I can check class times."
