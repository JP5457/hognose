from AiManager import AiManager

class PromptManager:
    def __init__(self, key):
        self.ai_manager = AiManager(key)
        self.universals = ["using python write some code to achieve the following task. Only return the functional python code: "]

    def stripcode(self, code):
        code = code.replace("```python\n", "")
        return code[:-3]

    def adduni(self, prompt):
        self.universals = [prompt] + self.universals

    def makecode(self, code):
        prompt = ""
        for i in self.universals:
            prompt+=i
        prompt += code
        pycode = self.ai_manager.generate_text(prompt)
        return self.stripcode(pycode)

    def makevariable(self, name, desc):
        prompt = ""
        for i in self.universals:
            prompt+=i
        prompt += "create a new variable with the name " + name + " with a sensible value based on the description " + desc
        pycode = self.ai_manager.generate_text(prompt)
        return self.stripcode(pycode)

    def makefunction(self, name, desc, inputs):
        prompt = ""
        for i in self.universals:
            prompt+=i
        prompt += "create a new function with the name " + name + " that takes the following inputs:\n"
        for i in inputs:
            prompt += i["name"] + " - " + i["desc"] + "\n"
        prompt += " the function should have the following function: " + desc
        pycode = self.ai_manager.generate_text(prompt)
        return self.stripcode(pycode)
