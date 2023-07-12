#!/usr/bin/env python3

import time
import signal
from methods import print_stdout, print_status
from blocks.volume import block_volume
from blocks.microphone import block_microphone
from blocks.battery import block_battery
from blocks.time import block_time

def update_status():
    blocks_list = []
    blocks_list.append(block_volume())
    blocks_list.append(block_microphone())
    blocks_list.append(block_battery())
    blocks_list.append(block_time())
    print_status(blocks_list)

def sigcont_handler(signum, frame):
    update_status()

# update status immediately upon bar being shown
signal.signal(signal.SIGCONT, sigcont_handler)

if __name__ == '__main__':
    # Print version header + the opening bracket
    print_stdout('{"version" : 1}[')

    # Continuously update the status line
    while True:
        update_status()
        time.sleep(1)
