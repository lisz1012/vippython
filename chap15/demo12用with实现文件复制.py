
# Author: lisz1012
# Creation date and time: 6/2/24 6:51 PM

with open('logo.png', 'rb') as file:
    with open('logo2.png', 'wb') as file2:
        file2.write(file.read())