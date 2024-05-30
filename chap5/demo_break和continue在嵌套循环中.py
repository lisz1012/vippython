# Author: lisz1012
# Creation date and time: 5/27/24 7:46 PM

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()
