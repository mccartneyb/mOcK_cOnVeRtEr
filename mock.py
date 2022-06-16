import os
import time

try:
    import pyperclip
except ImportError:
    os.system('pip install pyperclip')


string_to_convert = input('Enter the string to mock:\n')
string_converted = ''
exemptions = '?!@#$%^&*()_- '
count = 0

for char in string_to_convert:
    if char in exemptions:
        string_converted+=char
        continue
    if count%2==0:
        string_converted+=char.lower()
        count +=1
    else:
        string_converted+=char.upper()
        count +=1

pyperclip.copy(string_converted)
print(f"'{string_converted}' has been copied to clipboard.")
time.sleep(3)