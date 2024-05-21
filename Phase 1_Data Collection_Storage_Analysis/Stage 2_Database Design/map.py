import decimal
import math
from db import DeviceType


class Device:
    type: DeviceType = property(
        fget=lambda self: getattr(self, "__type", None),
        fset=lambda self, value: setattr(self, "__type", value),
        fdel=lambda self: delattr(self, "__type")
    )
    brand: str = property(
        fget=lambda self: getattr(self, "__brand", None),
        fset=lambda self, value: setattr(self, "__brand", value),
        fdel=lambda self: delattr(self, "__brand")
    )
    url: str = property(
        fget=lambda self: getattr(self, "__url", None),
        fset=lambda self, value: setattr(self, "__url", value),
        fdel=lambda self: delattr(self, "__url")
    )
    name: str = property(
        fget=lambda self: getattr(self, "__name", None),
        fset=lambda self, value: setattr(self, "__name", value),
        fdel=lambda self: delattr(self, "__name")
    )


def convert(entry: dict[str, object]) -> dict[str, object]:
    result: dict[str, object] = {

    }

    return result


def convert_mm_to_inches(entry: decimal) -> decimal:
    return entry / 25.4


def screen_size_to_body_size_ratio(width: decimal,
                                   height: decimal,
                                   display: decimal,
                                   resolution_x: decimal,
                                   resolution_y: decimal) -> decimal:
    width = convert_mm_to_inches(width)
    height = convert_mm_to_inches(height)

    aspect_screen = max(resolution_x, resolution_y) / min(resolution_x, resolution_y)
    device_area = width * height
    screen_x = width_from_diagonal(display, aspect_screen)
    screen_y = height_from_diagonal(display, aspect_screen)
    screen_area = screen_x * screen_y
    return math.ceil((screen_area / device_area) * 100)


def width_from_diagonal(diagonal: decimal, aspect: decimal) -> decimal:
    return diagonal * math.sin(math.atan(aspect))


def height_from_diagonal(diagonal: decimal, aspect: decimal) -> decimal:
    return diagonal * math.cos(math.atan(aspect))
