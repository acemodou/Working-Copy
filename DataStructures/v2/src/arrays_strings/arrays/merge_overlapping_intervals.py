from validate_answers import simple_assert
# def mergeOverlappingIntervals(intervals):
#     intervals.sort(key= lambda x : x[0])
#     overlapping = []
#     start, end = intervals[0]
    
#     for i in range(1, len(intervals)):
#         currStart, currEnd = intervals[i]
#         if end < currStart:
#             overlapping.append([start, end])
#             start = currStart
#             end = currEnd
#         else:
#             end = max(end, currEnd)
#     overlapping.append([start, end])
#     return overlapping

def mergeOverlappingIntervals(intervals):
 intervals.sort(key = lambda x : x[0])
 overlappingIntervals = [intervals[0]]
 for start, end in intervals[1:]:
     
     if start > overlappingIntervals[-1][1]:
         overlappingIntervals.append([start, end])
     else:
         overlappingIntervals[-1] = [overlappingIntervals[-1][0], max(overlappingIntervals[-1][1], end)]
 return overlappingIntervals

# intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# expected = [[1, 2], [3, 8], [9, 10]]
intervals = [[1, 22],[-20, 30]]
expected = [[-20, 30]]
actual = mergeOverlappingIntervals(intervals)
simple_assert(actual, expected)

