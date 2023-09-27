def sort_word(word):
    if len(word) <= 1:
        return word

    divider = word[len(word) // 2]
    left = "".join([letter for letter in word if letter < divider])
    middle = "".join([letter for letter in word if letter == divider])
    right = "".join([letter for letter in word if letter > divider])

    return sort_word(left) + middle + sort_word(right)


def is_anagram(first_string, second_string):
    first_string_sorted = sort_word(first_string.lower())
    second_string_sorted = sort_word(second_string.lower())

    if not first_string or not second_string:
        return (first_string_sorted, second_string_sorted, False)
    is_anagram_string = first_string_sorted == second_string_sorted

    return first_string_sorted, second_string_sorted, is_anagram_string
