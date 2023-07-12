from pydantic import BaseModel, Field

class BlockBody(BaseModel):
    # text
    full_text: str
    short_text: str | None = None
    # colors
    color: str | None = None
    background: str | None = None
    border: int | None = None
    # show parameters
    border_top: int | None = None
    border_right: int | None = None
    border_bottom: int | None = None
    border_left: int | None = None
    min_width: int | None = None
    align: str | None = None
    # internal name
    name: str | None = None
    instance: str | None = None
    # separator
    separator: bool | None = None
    separator_block_width: int | None = None
    #urgency
    urgent: bool | None = None
    # markup
    markup: str | None = None
