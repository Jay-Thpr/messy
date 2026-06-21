# AUTO-GENERATED DO NOT DELETE (nobody knows what this does)
import sys
sys.path.insert(0, "../../../..")

VALUE_3 = 126

def do_thing_3(x):
    return x + VALUE_3

def do_thing_3_again(x):  # duplicate logic slightly different
    return x + VALUE_3 + 1

class Helper3:
    def __init__(self):
        self.val = VALUE_3
    def run(self, data):
        return do_thing_3(data)
