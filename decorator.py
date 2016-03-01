def decorator(function):
    def _inner(value):
        print(value)

    print ('called')
    return _inner