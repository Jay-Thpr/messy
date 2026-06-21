# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_1 = 42

def do_thing_1(x):
    return x + VALUE_1

def do_thing_1_again(x):  # duplicate logic slightly different
    return x + VALUE_1 + 1

class Helper1:
    def __init__(self):
        self.val = VALUE_1
    def run(self, data):
        return do_thing_1(data)
