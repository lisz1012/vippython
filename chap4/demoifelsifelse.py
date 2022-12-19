# Author: lisz1012
# Creation date and time: 12/17/22 8:57 PM

score = 88
if 90 <= score <= 100:
    print("优")
elif 80 <= score < 90:
    print("良")
elif 60 <= score < 80:
    print("及格")
elif 0 <= score < 60:
    print("失败")
else:
    print("成绩非法")