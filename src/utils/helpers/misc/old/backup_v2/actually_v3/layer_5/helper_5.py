# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_5 = 210

def do_thing_5(x):
    return x + VALUE_5

def do_thing_5_again(x):  # duplicate logic slightly different
    return x + VALUE_5 + 1

class Helper5:
    def __init__(self):
        self.val = VALUE_5
    def run(self, data):
        return do_thing_5(data)
