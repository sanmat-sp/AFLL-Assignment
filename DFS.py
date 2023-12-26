"""Python3 program to implement DFS that accepts a language of strings that accepts even number of a's followed by at least one b."""


def start(c):
    if c == "a":
        dfa = 1
    elif c == "b":
        dfa = 3
    # -1 is used to check for any
    # invalid symbol
    else:
        dfa = -1
    return dfa


def state1(c):
    if c == "a":
        dfa = 2
    elif c == "b":
        dfa = 4
    else:
        dfa = -1
    return dfa


# This function is for the second
# dfa = state of DFA
def state2(c):
    if c == "b":
        dfa = 3
    elif c == "a":
        dfa = 1
    else:
        dfa = -1
    return dfa


# This function is for the third
# dfa = state of DFA
def state3(c):
    if c == "b":
        dfa = 3
    elif c == "a":
        dfa = 4
    else:
        dfa = -1
    return dfa


# This function is for the fourth
# dfa = state of DFA
def state4(c):
    dfa = -1
    return dfa


def isAccepted(String):
    # dfa tells the number associated
    # with the present dfa = state
    dfa = 0
    for i in range(len(String)):
        if dfa == 0:
            dfa = start(String[i])

        elif dfa == 1:
            dfa = state1(String[i])

        elif dfa == 2:
            dfa = state2(String[i])

        elif dfa == 3:
            dfa = state3(String[i])

        elif dfa == 4:
            dfa = state4(String[i])
        else:
            return 0
    if dfa == 3:
        return 1
    else:
        return 0


String = input()
if isAccepted(String):
    print("1")
else:
    print("0")
