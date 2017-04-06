"""Transform camelcase into kebab case string."""


def kebabize(string):
    new_string = ''
    for idx, item in enumerate(string):
        if item.isupper():
            if len(new_string) > 0 and string[idx - 1] is not '-':
                new_string += '-'
            new_string += item.lower()
        elif item.islower():
            new_string += item
        elif item is '-' and len(new_string) > 0 and string[idx - 1] is not '-':
            new_string += '-'
    return new_string
