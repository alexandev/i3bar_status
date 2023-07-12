import re
from models import BlockBody
from methods import cmd
from colors import COLOR_NORMAL, COLOR_IDLE, COLOR_WARNING

def block_volume():
    cmd_return = cmd("pactl get-sink-volume @DEFAULT_SINK@")

    volume = re.search('[0-9]{1,4}%', cmd_return)
    if volume != None :
        volume = volume.group()
    else :
        volume = False

    match volume :
        case _ if volume :
            if int(volume[:-1]) > 0 :
                return BlockBody(
                    full_text = " " + volume,
                    color = COLOR_NORMAL
                )
            else :
                return BlockBody(
                    full_text = "",
                    color = COLOR_IDLE
                )
        case other :
            return BlockBody(
                full_text = "volume error",
                color = COLOR_WARNING
            )
