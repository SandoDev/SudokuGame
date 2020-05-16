"""Utilities for views"""


def generate_title(sub: str, length: int, complement: str = '-') -> str:
    # TODO evoluciona para que tenga una longitud de alto y colores
    """
    Generate a subtittle with specific length

    Parameters
    ----------
        sub: str
            text string with subtitle
        length: int
            length of width the subtitle must have
        complement: str
            character with which to complement the desired length

    Returns
    ----------
        final_title: str
    """
    final_title = ""
    len_sub = len(sub)
    value = length-len_sub
    left = 0
    rigth = 0
    side_value = 0
    complement = complement
    separator = ""
    if len_sub < length:
        separator = " "
    elif len_sub == length:
        return sub
    else:
        for i in range(length):
            final_title = final_title + complement
        return final_title

    if value % 2 == 0:
        side_value = int(value/2)-1
        for i in range(length):
            if i < side_value:
                final_title = final_title + complement
            elif i > (side_value+len_sub)+1:
                final_title = final_title + complement
            elif (side_value+len_sub)+1 == i:
                final_title = final_title + separator + sub + separator
    else:
        left = int((value - 1)/2)
        rigth = left+1+len_sub
        for i in range(length):
            if i < left:
                final_title = final_title + complement
            elif i > rigth:
                final_title = final_title + complement
            elif left+1 == i:
                final_title = final_title + separator + sub + separator

    return final_title
