# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_12 = 504

def do_thing_12(x):
    return x + VALUE_12

def do_thing_12_again(x):  # duplicate logic slightly different
    return x + VALUE_12 + 1

class Helper12:
    def __init__(self):
        self.val = VALUE_12
    def run(self, data):
        return do_thing_12(data)
