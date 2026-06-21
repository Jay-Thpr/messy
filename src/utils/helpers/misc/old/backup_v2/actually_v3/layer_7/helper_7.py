# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_7 = 294

def do_thing_7(x):
    return x + VALUE_7

def do_thing_7_again(x):  # duplicate logic slightly different
    return x + VALUE_7 + 1

class Helper7:
    def __init__(self):
        self.val = VALUE_7
    def run(self, data):
        return do_thing_7(data)
