# AI Assistance Notes

I used ChatGPT for help understanding object-oriented programming,
fixing indentation errors, and building parts of this lab.

## Classes Generated With AI

ChatGPT helped generate the StockLookup, ClassSchedule,
and PilatesAssistant classes.

The original AI-generated class code is included in the
corresponding Python files.

## Code Explanations

- `class` defines a blueprint for objects.
- `__init__` sets up an object's starting attributes.
- `self` refers to the specific object.
- `self.stock` stores product inventory.
- `self.schedule` stores available class times.
- `self.history` stores the conversation.
- `find_product()` searches for a product.
- `count_for()` returns the product quantity.
- `find_day()` searches for a day.
- `times_for()` returns available class times.
- `respond()` records messages and returns replies.
- `choose_reply()` selects responses using keyword rules.
- `return None` indicates that no match was found.
## Module 11 — AI Assistance
### EchoModel Code

ChatGPT helped me write and understand the EchoModel class for Exercise 2.

```python
class EchoModel:
    def reply(self, instructions, history):
        return "You said: " + history[-1]["content"]
```

### Code Explanations

- `class EchoModel:` creates a class that acts as a simple model.
- `def reply(self, instructions, history):` defines a method that receives the chatbot's instructions and conversation history.
- `return "You said: " + history[-1]["content"]` gets the last message from the conversation and returns it with "You said: " in front.

I also used ChatGPT to help connect MockModel to SupportChatbot, troubleshoot errors, and update my tests. I reviewed the changes and verified that all 15 tests passed.