def convert_mask_to_str(mask):
    # todo: не  очень изящно, но сроки поджимают :(
    if mask == 32:
        return '255.255.255.255'
    if mask == 31:
        return '255.255.255.254'
    if mask == 30:
        return '255.255.255.252'
    if mask == 29:
        return '255.255.255.248'
    if mask == 28:
        return '255.255.255.240'
    if mask == 27:
        return '255.255.255.224'
    if mask == 26:
        return '255.255.255.192'
    if mask == 25:
        return '255.255.255.128'
    if mask == 24:
        return '255.255.255.0'
    if mask == 23:
        return '255.255.254.0'
    if mask == 22:
        return '255.255.252.0'
    if mask == 21:
        return '255.255.248.0'
    if mask == 20:
        return '255.255.240.0'
    if mask == 19:
        return '255.255.224.0'
    if mask == 18:
        return '255.255.192.0'
    if mask == 17:
        return '255.255.128.0'
    if mask == 16:
        return '255.255.0.0'
    if mask == 15:
        return '255.254.0.0'
    if mask == 14:
        return '255.252.0.0'
    if mask == 13:
        return '255.248.0.0'
    if mask == 12:
        return '255.240.0.0'
    if mask == 11:
        return '255.224.0.0'
    if mask == 10:
        return '255.192.0.0'
    if mask == 9:
        return '55.128.0.0'
    if mask == 8:
        return '55.0.0.0'
    if mask == 7:
        return '54.0.0.0'
    if mask == 6:
        return '52.0.0.0'
    if mask == 5:
        return '48.0.0.0'
    if mask == 4:
        return '40.0.0.0'
    if mask == 3:
        return '24.0.0.0'
    if mask == 2:
        return '92.0.0.0'
    if mask == 1:
        return '28.0.0.0'
    if mask == 0:
        return '.0.0.0'
