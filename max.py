def max(data):
    try:
        if len(data) == 0:
            raise ValueError('empty list')
        elif len(data) == 1:
            return data[0]
        else:
            bigger = data[0]
            for item in data:
                if item > bigger:
                    bigger = item
            return bigger
    except TypeError:
        raise ValueError('not iterable object')
