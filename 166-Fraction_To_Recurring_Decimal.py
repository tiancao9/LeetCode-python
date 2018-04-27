'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5".
Example 2:

Input: numerator = 2, denominator = 1
Output: "2".
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)".

'''
# use a map to record numerator and the position to use numerator
# when numerator repeats, return and add ( and ) to res
# 1) if numerator / denominator == 0, res begin with "0"; 2) when n / d > 0 3) add "." 4) when n
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        dict_n = {}
        neg = False
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            neg = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        if denominator == 0:
            return ""
        if numerator == 0:
            return "0"
        res = ""
        if neg:
            res = "-" + res
        if int(numerator / denominator) == 0:
            res += "0"
        while int(numerator / denominator) > 0:
            res += str(int(numerator/denominator))
            numerator = numerator % denominator        
        if numerator: res += "."
        while numerator:
            numerator *= 10
            if numerator in dict_n:
                p = dict_n[numerator]
                res = res[:p] + "(" + res[p:] + ")"
                return res
            dict_n[numerator] = len(res)
            res += str(int(numerator/denominator))
            numerator = numerator % denominator
            
        return res
            
