def optalgo_frequent_words(subject, k):
    """This function searches for the most frequent pattern in a subject string"""
    # We need re module for the string search in the helper function
    import re

    def pattern_count(subject, pattern):
        """Helper function that counts the occurrences of a given pattern in a subject string"""
        count = 0

        # we need to use a lookahead assertion. Lookaheads don't consume the string durning the match
        # We will return an empty match since a lookahead is only a precursor element prepend the actuall match
        for i in re.finditer(r'(?=({}))'.format(pattern),subject):
            count += 1

        return count

    # dictionary that stores all experienced patterns
    frequent_patterns = {}

    # use a sliding-window with size k to scan the subject string
    for i in range(len(subject) - k + 1):
        pattern = subject[i:i+k]

        # compute only new patterns since old ones are allready counted
        if pattern not in frequent_patterns:
            frequent_patterns[pattern] = pattern_count(subject, pattern)

    return max(frequent_patterns.items(), key=lambda item: item[1])
