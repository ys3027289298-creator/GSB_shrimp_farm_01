import json

TRANSFER_AMOUNT = 10
SCHEDULE_TIME = (10, 3)
NEGATIVE_AMOUNT = -5
NEGATIVE_TRANSFER = -10
MULTISTEP_VALUE = 8
MULTISTEP_LOG = ("op", "failed")


def new_game():
    return {'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'queue': [], 'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'count': 0, 'closed': False, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}


def bug_12(state, amount=TRANSFER_AMOUNT):
    if state["closed"] or state["settled"]:
        return False
    if not isinstance(amount, int) or amount < 0 or state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True


def bug_19(state):
    if state["closed"] or state["settled"]:
        return False
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True


def bug_26(state, event=SCHEDULE_TIME):
    if state["closed"] or state["settled"]:
        return False
    start, end = event
    if not isinstance(start, int) or not isinstance(end, int) or start >= end:
        return False
    next_id = (max(state["events"]) + 1) if state["events"] else 1
    state["events"][next_id] = (start, end)
    return True


def bug_3(state):
    if state["closed"] or state["settled"] or not state["queue"]:
        return False
    return state["queue"].pop(0)


def bug_10(state, amount=NEGATIVE_AMOUNT):
    if state["closed"] or state["settled"]:
        return False
    if not isinstance(amount, int) or amount < 0:
        return False
    state["amount"] += amount
    return True


def bug_17(state, amount=NEGATIVE_TRANSFER):
    if state["closed"] or state["settled"]:
        return False
    if not isinstance(amount, int) or amount < 0 or state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True


def bug_24(state):
    if not state["events"]:
        return None
    return min(state["events"].items(), key=lambda item: item[1][0])[0]


def bug_1(state):
    if state["closed"] or state["settled"]:
        return False
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True


def bug_8(state):
    state["count"] = 0
    state["amount"] = 0
    state["slots"] = 0
    return True


def bug_15(state):
    if state["closed"] or state["settled"]:
        return False
    state["closed"] = True
    return True


def bug_30(state):
    if state["closed"] or state["settled"]:
        return False
    state["value"] = MULTISTEP_VALUE
    state["log"].append(MULTISTEP_LOG)
    if any(entry[1] == "failed" for entry in state["log"]):
        state["value"] = state["snapshot"]
        return False
    state["snapshot"] = state["value"]
    return True


def bug_31(state):
    if state["closed"] or state["settled"]:
        return False
    state["settled"] = True
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
        if raw == "run":
            state = new_game()
            print(json.dumps({"step": "bug_12_fail_no_debit", "ok": bug_12(state), "state": state}))
            state["slots"] = state["cap"]
            print(json.dumps({"step": "bug_19_full_rejected", "ok": bug_19(state), "slots": state["slots"]}))
            state = new_game()
            print(json.dumps({"step": "bug_26_bad_range_rejected", "ok": bug_26(state), "events": state["events"]}))
            state["queue"] = [1, 2]
            print(json.dumps({"step": "bug_3_fifo", "first": bug_3(state), "queue": state["queue"]}))
            print(json.dumps({"step": "bug_10_negative_rejected", "ok": bug_10(state), "amount": state["amount"]}))
            print(json.dumps({"step": "bug_17_negative_rejected", "ok": bug_17(state), "src": state["src"], "dst": state["dst"]}))
            print(json.dumps({"step": "bug_24_earliest", "event": bug_24(state)}))
            state["items"] = ["a", "b"]
            print(json.dumps({"step": "bug_1_full_rejected", "ok": bug_1(state), "items": state["items"]}))
            state["count"] = 5
            bug_8(state)
            print(json.dumps({"step": "bug_8_reset_stats", "count": state["count"], "amount": state["amount"], "slots": state["slots"]}))
            state = new_game()
            state["closed"] = True
            print(json.dumps({"step": "bug_15_closed_blocks", "ok": bug_15(state)}))
            state = new_game()
            state["value"] = MULTISTEP_VALUE
            state["log"] = [("op", "failed")]
            print(json.dumps({"step": "bug_30_rollback", "ok": bug_30(state), "value": state["value"], "log": state["log"]}))
            state = new_game()
            bug_31(state)
            print(json.dumps({"step": "bug_31_settled_blocks_write", "write_ok": bug_12(state), "settled": state["settled"]}))
        else:
            print("ok")


if __name__ == "__main__":
    main()
