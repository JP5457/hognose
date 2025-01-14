import sys
from LexManager import LexManager

def main():
    args = sys.argv
    if len(args)!=4:
        print("hognose [input] [output] [apikey]")
    else:
        hognose = args[1]
        output = args[2]
        apikey = args[3]
        with open(hognose, "r") as file:
            lines = file.readlines()
        lex_manager = LexManager(lines, apikey)
        program = lex_manager.compile()
        if program != None:
            with open(output, "w") as file:
                file.write(program)
        print("program successfully written to " + output)

if __name__ == '__main__':
    main()
