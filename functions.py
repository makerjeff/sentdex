#define a repeat function that takes 2 arguments
def repeat(string, iteration, exclaim):
    """
    Returns a string a set number of times.
    :param string: String duplicate.
    :param iteration: Number of times to duplicate.
    :param exclaim: If this is true, add exclamation marks.
    :return: Result of the strings.
    """
    result = string * iteration
    if exclaim:
        result = result + '!!!'

    result = result + '\n'
    return result

print(repeat('something', 10, True))
print(repeat('nothing', 5, False))
print(repeat.__doc__)
