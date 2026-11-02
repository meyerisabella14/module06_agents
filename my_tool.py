# my_tool.py
# Author: Isabella Meyer


class ClassSchedule:
    """Stores available Pilates class times."""

    def __init__(self, schedule):
        # Save the class schedule for this tool.
        self.schedule = schedule

    def find_day(self, text):
        # Check whether the message mentions a known day.
        for day in self.schedule:
            # Ignore differences in capitalization.
            if day.lower() in text.lower():
                return day

        # No matching day was found.
        return None

    def times_for(self, day):
        # Return class times if the day exists.
        if day in self.schedule:
            return self.schedule[day]

        # Return None for an unknown day.
        return None
