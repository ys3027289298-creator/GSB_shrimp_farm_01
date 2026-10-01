import json


def new_game():
    return {'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'queue': [], 'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'count': 0, 'closed': False, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_12(state):
    amount = 10
    if amount <= 0 or state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_19(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def bug_26(state):
    last_end = None
    for event_id in sorted(state["events"]):
        start, end = state["events"][event_id]
        if start >= end:
            return False
        if last_end is not None and start < last_end:
            return False
        last_end = end
    return True

def bug_3(state):
    if not state["queue"]:
        return None
    return state["queue"].pop(0)

def bug_10(state):
    amount = -5
    if amount < 0:
        return False
    state["amount"] += amount
    return True

def bug_17(state):
    amount = state["amount"]
    if amount <= 0 or state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_24(state):
    if not state["events"]:
        return None
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def bug_8(state):
    state["count"] = 0
    state["amount"] = 0
    state["queue"] = []
    state["items"] = []
    state["log"] = []
    return True

def bug_15(state):
    if state["closed"]:
        return False
    return True

def bug_30(state):
    if any(status == "failed" for _, status in state["log"]):
        state["value"] = state["snapshot"]
        return False
    state["snapshot"] = state["value"]
    return True

def bug_31(state):
    if state["settled"]:
        return False
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
