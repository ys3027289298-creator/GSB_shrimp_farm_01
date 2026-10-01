import json


def new_game():
    return {'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'queue': [], 'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'count': 0, 'closed': False}

def bug_12(state):
    state["src"] -= 10
    return True

def bug_19(state):
    return True

def bug_26(state):
    return True

def bug_3(state):
    return state["queue"].pop()

def bug_10(state):
    state["amount"] += -5
    return True

def bug_17(state):
    return True

def bug_24(state):
    return max(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    state["items"].append("x")
    return True

def bug_8(state):
    return True

def bug_15(state):
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
