# Find the minimum minutes difference


timePoints = ["23:59","00:00"]
# 1. Convert Hours into minutes
minutes=[]
for i in range(len(timePoints)):
    curr=timePoints[i]
    total_minutes=int(curr[0:2])*60+int(curr[3:])
    minutes.append(total_minutes)
# 2. Sort the Array to check difference
minutes.sort()
# 3 . Compare difference of the minutes
mini=1440
for i in range(1,len(minutes)):
    diff=minutes[i]-minutes[i-1]
    mini=min(mini,diff)
last_diff=(minutes[0]+1440)-minutes[len(minutes)-1]
mini=min(mini,last_diff)
print(mini)
 

# Output will be : 1