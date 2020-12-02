def is_isogram(string):
    # Lowercases. Remove spaces and hyphens
    string = string.lower()
    string = string.replace(' ', '').replace('-', '')

    # Check if length match
    return len(string) == len(set(string))
