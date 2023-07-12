import time
from models import BlockBody
from colors import COLOR_NORMAL

def block_time():
    current_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
    return BlockBody(
        full_text = current_time,
        color = COLOR_NORMAL
    )
