nums = input("please input your numbers: ")
seperator = input("input your seperator character:(, . / space...) ")
print("length of your number series is :", len(nums))
mynum = []
length = len(nums)
b = ""

for i in range(length):
    if nums[i] != seperator:
        b = b+nums[i]
    else:
        mynum = mynum+[int(b)]
        b = ""
    if i == length-1:
        mynum = mynum+[int(b)]
print(mynum)
