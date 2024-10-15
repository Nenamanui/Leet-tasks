# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.curr_list = nestedList
        self.flattenedList = []
        self.index = 0
        
        def flatten(currentList):
            for point in currentList:
                if point.isInteger():
                    self.flattenedList.append(point.getInteger())
                else:
                    flatten(point.getList())
        flatten(self.curr_list)

    
    def next(self) -> int:
        point = self.flattenedList[self.index]
        self.index += 1
        return point
        
    
    def hasNext(self) -> bool:
        return self.index < len(self.flattenedList)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next()) 
