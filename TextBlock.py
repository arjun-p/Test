def text_sanity_checker(lines):
    """ Validates each line of prose.
    Lines should contain between 1 and 50 elements, inclusive.
    Each element of lines should contain between 1 and 50 characters, inclusive.
    Each element of lines should contain the same number of characters.
    Each character in lines should be an uppercase letter ([A-Z]).

    Args:
        lines : list of strings to validate
    Returns:
        True if all elements are in the correct format
    Raises:
        ValueError: if the list length is out of range or the elements are not in the specified format
    """
    MAX_ELEMENTS = 50
    MAX_CHARACTERS = 50

    if not lines or len(lines) > MAX_ELEMENTS:
        raise ValueError('Input should contain between 1 and %d elements, inclusive.' % MAX_ELEMENTS)

    character_count = len(lines[0])
    if character_count < 1 or character_count > MAX_CHARACTERS:
        raise ValueError(
            'Each element of input should contain between 1 and %d characters, inclusive.' % MAX_CHARACTERS)

    for word in lines:
        if len(word) != character_count:
            raise ValueError(
                'Each element of input should contain the same number of characters (between 1 and %d, inclusive).' % (
                    MAX_CHARACTERS))

    if not ''.join(lines).isupper():
        raise ValueError('Each character in input should be an uppercase letter ([A-Z]).')


def text_blocker(lines):
    """Returns a list of strings that is read "downward".
    First element of lines will correspond to the first "column" of the returned list, and so forth.

    Args:
        lines : list of strings to concatenate vertically (downward)
    Returns:
        list of strings
    """
    try:
        text_sanity_checker(lines)

        result = []
        line_len = len(lines)
        element_len = len(lines[0])

        line_counter = 0
        element_counter = 0

        while element_counter < element_len:
            vertical_list = []
            while line_counter < line_len:
                vertical_list.append(lines[line_counter][element_counter])
                line_counter += 1
            result.append(''.join(vertical_list))
            element_counter += 1
            line_counter = 0
        return result
    except ValueError as e:
        print('Error: ', e)
