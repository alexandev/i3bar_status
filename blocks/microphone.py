import re
from models import BlockBody
from methods import cmd
from colors import COLOR_IDLE, COLOR_WARNING

def block_microphone():
    cmd_return = cmd("pactl get-source-mute @DEFAULT_SOURCE@")

    # find line that starts with text, then split it at the ':' symbol and strip all spaces
    mute = re.search('Mute:.+', cmd_return)
    if mute != None :
        mute = mute.group().split(':')[1].strip()
    else :
        mute = False

    match mute :
        case "yes" :
            return BlockBody(
                full_text = "",
                color = COLOR_IDLE
            )
        case "no" :
            return BlockBody(
                full_text = "",
                color = COLOR_WARNING
            )
        case other :
            return BlockBody(
                full_text = "microphone error",
                color = COLOR_WARNING
            )
