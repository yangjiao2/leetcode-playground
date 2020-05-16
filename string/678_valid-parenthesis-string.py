# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# When * is introduced, the number becomes a range,
# indicating the number of possible unmatched found.
# One * just expand the range by 1
# And we can use the same principle to check if the criteria above is within the range.


class Solution:
    def checkValidString(self, s: str) -> bool:
        high, low = 0, 0
        for i in s:
            if i == '(':
                high += 1
                low += 1
            elif i == ')':
                high -= 1
                low -= 1
            else:
                high += 1
                low -= 1
            low = max(low, 0)
            if high < 0:
                return False
        return low == 0