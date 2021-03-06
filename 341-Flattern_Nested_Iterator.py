'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#Use stack, everytime we check hasNext(), make sure the 1st item in stack is integer, other wise, pop, unlisted and put in
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        i = len(nestedList)-1
        while i >= 0:
            self.stack.append(nestedList[i])
            i -= 1
    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0:
            cur = self.stack.pop()
            if cur.isInteger():
                self.stack.append(cur)
                return True
            else:
                temp = cur.getList()
                i = len(temp)-1
                while i >= 0:
                    self.stack.append(temp[i])
                    i -= 1
        return False
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

