from PromptManager import PromptManager
import re

class LexManager:
    def __init__(self, lines, key):
        self.prompt_manager = PromptManager(key)
        self.lines = lines

    def replaceinprompt(self, prompt, variables, functions):
        for var in variables:
            torep = var["name"] + " (where " + var["name"] + " is a pre-existing variable that should not be declared with the description \"" + var["desc"] +"\")"
            prompt = prompt.replace("||"+var["name"]+"/", torep)
        for func in functions:
            torep = func["name"] + " (where " + func["name"] + " is a pre-existing function that should not be declared with the description \"" + func["desc"] +"\" that takes the inputs: "
            for i in func["inputs"]:
                torep += i["name"] + " - " + i["desc"]
            prompt = prompt.replace("!!"+func["name"]+"/", torep)
        statics = re.findall(";;.*/", prompt)
        for i in statics:
            torep = i[2:-1] + " (which is a static value)"
            prompt = prompt.replace(i, torep)
        return prompt

    def verifyname(self, name):
        return name.isalpha()

    def printerror(error, line):
        print("error: \""+error +"\" in line \"" + line + "\"")

    def compile(self):
        variables = []
        functions = []
        state = "general"
        program = ""
        newlines = []
        line = ""

        for i in self.lines:
            i = i.strip()
            if i[-2:] == "&&":
                line+=i[:-2]
                continue
            line += i
            if line != "":
                newlines.append(line)
                line = ""
        
        for line in newlines:
            if line[0:4] == "||^/":
                prompt = self.replaceinprompt(line[4:], variables, functions)
                code = self.prompt_manager.makecode(prompt)
                program += code

            elif line[0:4] == "||*/":
                prompt = self.replaceinprompt(line[4:], variables, functions)
                self.prompt_manager.adduni(prompt)

            elif line[0:3] == "<||":
                try:
                    x = line.find("/")
                except:
                    self.printerror("expected /", line)
                    return None
                name = line[3:x]
                desc = self.replaceinprompt(line[x+1:], variables, functions)
                if self.verifyname(name):
                    variables.append({"name": name, "desc": desc})
                    code = self.prompt_manager.makevariable(name, desc)
                    program += code
                else:
                    self.printerror("names must be alpha without spaces", line)
                    return None

            elif line[0:3] == "<!!":
                try:
                    x = line.find("/")
                except:
                    self.printerror("expected /", line)
                    return None
                params = line[3:x]
                desc = self.replaceinprompt(line[x+1:], variables, functions) 
                inputs = []
                if "<" in params:
                    indexesopen = [x for x, v in enumerate(params) if v == '<']
                    indexesclose = [x for x, v in enumerate(params) if v == '>']
                    name = params[0:indexesopen[0]]
                    if not self.verifyname(name):
                        self.printerror("names must be alpha without spaces", line)
                        return None
                    if len(indexesclose) != len(indexesopen):
                        self.printerror("paramaters formated incorrectly", line)
                        return None
                    for i in range(0, len(indexesopen)):
                        start = indexesopen[i]
                        end = indexesclose[i]
                        if end < start:
                            self.printerror("paramaters formated incorrectly", line)
                            return None
                        param = params[start+1:end]
                        try:
                            param = param.split("|")
                        except:
                            self.printerror("expected |", line)
                            return None
                        if self.verifyname(param[0]):
                            inputs.append({"name": param[0], "desc": param[1] })
                        else:
                            self.printerror("names must be alpha without spaces", line)
                            return None
                else:
                    name = params
                functions.append({"name": name, "inputs": inputs, "desc": desc})
                code = self.prompt_manager.makefunction(name, desc, inputs)
                program += code

            else:
                self.printerror("syntax error", line)
                return None

        return program


                