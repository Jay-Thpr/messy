# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_8 = 336

def do_thing_8(x):
    return x + VALUE_8

def do_thing_8_again(x):  # duplicate logic slightly different
    return x + VALUE_8 + 1

class Helper8:
    def __init__(self):
        self.val = VALUE_8
    def run(self, data):
        return do_thing_8(data)
