from models import BlockBody
from methods import cmd
from colors import COLOR_IDLE, COLOR_WARNING

def block_microphone():
    cmd_return = cmd("pactl get-source-mute @DEFAULT_SOURCE@")
    if cmd_return.find("yes") == -1 :
        return BlockBody(
            full_text = "",
            color = COLOR_WARNING
        )
    else:
        return BlockBody(
            full_text = "",
            color = COLOR_IDLE
        )
