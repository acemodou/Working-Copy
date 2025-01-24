from validate_answers import simple_assert

def underscorifySubstring(string, substring):
    # Write your code here.
    def findSubstrLocation():
        startIdx = 0
        locations = []
        while startIdx < len(string):
            nextPos = string.find(substring, startIdx)
            if nextPos == -1:
                break 
            locations.append([nextPos, nextPos + len(substring)])
            startIdx = nextPos + 1
        return locations
    
    def mergeIntervals(locations):
        if not len(locations):
            return locations
        
        intervals = [locations[0]]
        for start, end in locations[1:]:
            if intervals[-1][1] >= start:
                intervals[-1][1] = end 
            else:
                intervals.append([start, end])
        return intervals 
            
    def insertUnderscore(intervals):
        underscorify = []
        
        prevIdx = 0 
        for start, end in intervals:
            underscorify.append(string[prevIdx:start])
            underscorify.append("_")
            underscorify.append(string[start:end])
            underscorify.append("_")
            prevIdx = end 
        underscorify.append(string[prevIdx:])
        return "".join(underscorify)
            
    location = findSubstrLocation()
    intervals = mergeIntervals(location)
    return insertUnderscore(intervals)


simple_assert(underscorifySubstring(
                "testthis is a testtest to see if testestest it works", "test"
            ),
            "_test_this is a _testtest_ to see if _testestest_ it works",
        )
