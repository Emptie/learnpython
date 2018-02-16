def get_formatted_name(first, last, middle=''):
    """返回一个整洁的名字"""
    if middle:
        full_name = first + " " + middle + ' ' + last
    else:
        full_name = first + " " + last
    return full_name.title()