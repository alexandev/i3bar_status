import re
from models import BlockBody
from methods import cmd
from colors import COLOR_NORMAL, COLOR_IDLE, COLOR_GOOD, COLOR_WARNING, COLOR_BAD

def block_battery():
    cmd_return = cmd("upower -i /org/freedesktop/UPower/devices/battery_BAT0")
    
    # find lines that start with text, then split them at the ':' symbol and strip all spaces
    state = re.search('state:.+', cmd_return).group().split(':')[1].strip()
    percentage = re.search('percentage:.+', cmd_return).group().split(':')[1].strip()

    match state :
        case 'fully-charged' :
            return BlockBody(
                full_text = " " + percentage,
                color = COLOR_IDLE
            )
        case 'pending-charge' :
            return BlockBody(
                full_text = " " + percentage,
                color = COLOR_GOOD
            )
        case 'charging' :
            return BlockBody(
                full_text = " " + percentage,
                color = COLOR_GOOD
            )
        case 'discharging' :
            percentage_int = int(percentage[:-1])
            match percentage_int :
                case _ if percentage_int >= 80 :
                    return BlockBody(
                        full_text = " " + percentage,
                        color = COLOR_NORMAL
                    )
                case _ if percentage_int >= 60 :
                    return BlockBody(
                        full_text = " " + percentage,
                        color = COLOR_NORMAL
                    )
                case _ if percentage_int >= 40 :
                    return BlockBody(
                        full_text = " " + percentage,
                        color = COLOR_NORMAL
                    )
                case _ if percentage_int >= 20 :
                    return BlockBody(
                        full_text = " " + percentage,
                        color = COLOR_WARNING
                    )
                case _ if percentage_int >= 0 :
                    return BlockBody(
                        full_text = " " + percentage,
                        color = COLOR_BAD
                    )
        case other :
            return BlockBody(
                full_text = state + " " + percentage,
                color = COLOR_WARNING
            )
