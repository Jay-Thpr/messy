# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_11 = 462

def do_thing_11(x):
    return x + VALUE_11

def do_thing_11_again(x):  # duplicate logic slightly different
    return x + VALUE_11 + 1

class Helper11:
    def __init__(self):
        self.val = VALUE_11
    def run(self, data):
        return do_thing_11(data)
