# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_9 = 378

def do_thing_9(x):
    return x + VALUE_9

def do_thing_9_again(x):  # duplicate logic slightly different
    return x + VALUE_9 + 1

class Helper9:
    def __init__(self):
        self.val = VALUE_9
    def run(self, data):
        return do_thing_9(data)
