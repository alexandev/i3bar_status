import re
from models import BlockBody
from methods import cmd
from colors import COLOR_NORMAL, COLOR_IDLE, COLOR_GOOD, COLOR_WARNING, COLOR_BAD

def block_battery():
    battery = "/org/freedesktop/UPower/devices/battery_BAT0"
    cmd_return = cmd("upower -i " + battery)
    
    # find line that starts with text, then split it at the ':' symbol and strip all spaces
    state = re.search('state:.+', cmd_return)
    if state != None :
        state = state.group().split(':')[1].strip()
    else :
        state = False

    percentage = re.search('percentage:.+', cmd_return)
    if percentage != None :
        percentage = percentage.group().split(':')[1].strip()
    else :
        percentage = False
    
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
                full_text = "battery error",
                color = COLOR_WARNING
            )
