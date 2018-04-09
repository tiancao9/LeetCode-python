'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''

# L==R, U==D -> True

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        L_nums = moves.count('L')
        R_nums = moves.count('R')
        U_nums = moves.count('U')
        D_nums = moves.count('D')
        if L_nums != R_nums or U_nums != D_nums:
            return False
        return True
