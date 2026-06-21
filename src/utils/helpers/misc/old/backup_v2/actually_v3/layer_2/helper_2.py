# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_2 = 84

def do_thing_2(x):
    return x + VALUE_2

def do_thing_2_again(x):  # duplicate logic slightly different
    return x + VALUE_2 + 1

class Helper2:
    def __init__(self):
        self.val = VALUE_2
    def run(self, data):
        return do_thing_2(data)
