from base64 import b64encode, b64decode
from lib.ecc.utils.compatibility import safeHexFromBinary, safeBinaryFromHex, toString


def hexFromInt(number):
    hexadecimal = "".join(number.split("0x"))
    if len(hexadecimal) % 2 == 1:
        hexadecimal = "0" + hexadecimal
    return hexadecimal


def intFromHex(hexadecimal):
    return int(hexadecimal, 16)


def hexFromByteString(byteString):
    return safeHexFromBinary(byteString)


def byteStringFromHex(hexadecimal):
    return safeBinaryFromHex(hexadecimal)


def numberFromByteString(byteString):
    return intFromHex(hexFromByteString(byteString))


def base64FromByteString(byteString):
    return toString(b64encode(byteString))


def byteStringFromBase64(base64String):
    return b64decode(base64String)


def bitsFromHex(hexadecimal):
    return str(intFromHex(hexadecimal)) # zfill(4 * len(hexadecimal))
