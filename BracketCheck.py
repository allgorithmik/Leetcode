def bracketCheck(brackets: list) -> bool:
    lis = []
    for i in range(len(brackets)):
        if brackets[i] == "{" and brackets[i + 1] == "}" and brackets.count("{") == brackets.count("}"):
            print("True for {}")
        elif brackets[i] == "(" and brackets[i + 1] == ")" and brackets.count("(") == brackets.count(")"):
            print("True for ()")
        elif brackets[i] == "[" and brackets[i + 1] == "]" and brackets.count("[") == brackets.count("]"):
            print("True for []")
        elif brackets[i] == "<" and brackets[i + 1] == ">"and brackets.count("<") == brackets.count(">"):
            print("True for <>")

bracketCheck() # pass a list of brackets as individial items **known bug exists**