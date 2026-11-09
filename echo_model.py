# echo_model.py
# Author: Isabella Meyer

class EchoModel:
        def reply(self, instructions, history):
                       return "You said: " + history[-1]["content"] 
        # echo_model.py
# Author: Isabella Meyer

# Creates a class that acts as a simple model.
class EchoModel:
    # Defines the method that receives instructions and conversation history.
    def reply(self, instructions, history):
        # Returns the latest message with "You said: " added before it.
        return "You said: " + history[-1]["content"]