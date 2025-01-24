from validate_answers import simple_assert
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updateCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updateCalendar2 = updateCalendar(calendar2, dailyBounds2)
    mergeCalendars = merge(updateCalendar1, updateCalendar2)
    flattenCalendar = flattenCalendars(mergeCalendars)
    return getMatchingAvailabilies(flattenCalendar, meetingDuration)
    
def updateCalendar(calendar, dailyBounds):
    calendarUpdate = calendar[:]
    calendarUpdate.insert(0, ["0:00", dailyBounds[0]])
    calendarUpdate.append([dailyBounds[1], "23:59"])
    return list(map(lambda m: [timeToMins(m[0]), timeToMins(m[1])], calendarUpdate))
    
def timeToMins(time):
    hour, mins = list(map(int, time.split(":")))
    return hour * 60 + mins 
   
def merge(list1, list2):
    i, j = 0, 0 
    mergedList = []

    while i < len(list1) and j < len(list2):
        m1, m2 = list1[i], list2[j]
        if m1[0] < m2[0]:
            mergedList.append(m1)
            i += 1 
        else:
            mergedList.append(m2)
            j += 1
    
    if i < len(list1):
        mergedList += list1[i:]
    if j < len(list2):
        mergedList += list2[j:]
    return mergedList

def flattenCalendars(calendar):
    if not len(calendar):
        return calendar
    
    flattenCalendar = calendar[:]
    overlappingIntervals = [flattenCalendar[0]]
    
    for start, end in flattenCalendar[1:]:
        if overlappingIntervals[-1][1] >= start:
            overlappingIntervals[-1][1] = max(overlappingIntervals[-1][1], end)
        else:
            
            overlappingIntervals.append([start, end])
    return overlappingIntervals

def getMatchingAvailabilies(calendar, meetingDuration):
    availability = []
    for i in range(1, len(calendar)):
        prevEndtime = calendar[i-1][1] 
        currStartTime = calendar[i][0]
        
        duration = currStartTime - prevEndtime
        if duration >= meetingDuration:
            availability.append([prevEndtime, currStartTime])
    return list(map(lambda t:  [minsToTime(t[0]), minsToTime(t[1])], availability))

def minsToTime(minute):
    hr = minute // 60
    mins = minute  % 60
    minsToString = '0'+ str(mins) if mins < 10 else str(mins)
    return f"{hr}:{minsToString}"     

calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30
expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
result = calendarMatching(
    calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
)
simple_assert(result, expected)
