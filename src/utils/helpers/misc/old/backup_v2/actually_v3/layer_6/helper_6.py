# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_6 = 252

def do_thing_6(x):
    return x + VALUE_6

def do_thing_6_again(x):  # duplicate logic slightly different
    return x + VALUE_6 + 1

class Helper6:
    def __init__(self):
        self.val = VALUE_6
    def run(self, data):
        return do_thing_6(data)
