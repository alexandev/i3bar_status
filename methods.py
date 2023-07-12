import sys
import subprocess
from models import BlockBody

def read_stdout():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

def print_stdout(message: str):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def cmd(cmd_str: str):
    output = subprocess.run(cmd_str, shell=True, capture_output=True)
    return output.stdout.decode('UTF-8')

def print_status(blocks_list: list[BlockBody]):
    print_stdout("[")
    for key, block in enumerate(blocks_list) :
        print_stdout(block.json())
        if key < len(blocks_list)-1 :
            print(",")
    print_stdout("],")
