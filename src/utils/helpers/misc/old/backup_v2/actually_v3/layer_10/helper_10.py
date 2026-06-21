# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_10 = 420

def do_thing_10(x):
    return x + VALUE_10

def do_thing_10_again(x):  # duplicate logic slightly different
    return x + VALUE_10 + 1

class Helper10:
    def __init__(self):
        self.val = VALUE_10
    def run(self, data):
        return do_thing_10(data)
