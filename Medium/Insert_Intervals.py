"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 
Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
class Solution:

    def merge(self, intervals, newInterval, i):
        #Endi >= Starti+1
        r = []
        start = min(intervals[i][0],newInterval[0])
        end = max(intervals[i][1],newInterval[1])
        return [start,end]
    def one_pass(self, intervals, newInterval):
        l = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                l.append(newInterval)
                return l + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                l.append(intervals[i])
            else:
                #once there is a merge -> merge until we cant
                newInterval = self.merge(intervals, newInterval, i)

if __name__ == "__main__":

    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    #output would be a list of list
    Sol = Solution()
    print(Sol.one_pass(intervals, newInterval))
    print("heelo")