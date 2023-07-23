def longestSuccessiveElements(a):
    hashSet = set()
    for num in a:
        hashSet.add(num)
    longestStreak = 0
    for num in a:
        if (num - 1) not in hashSet:
            currentNum = num
            currentStreak = 1
            while (currentNum + 1) in hashSet:
                currentNum += 1
                currentStreak += 1
            longestStreak = max(longestStreak, currentStreak)
    return longestStreak