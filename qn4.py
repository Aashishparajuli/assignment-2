import re

# with open('genius_club'.txt) as file :
#    reader=file.read()
#    print(reader)

pattern=r'[+\d{3}-\d{10}|+\d{2}-\d{6}]'
sequence=' asdjshd +977-9841585917 +01-565859 asdksjad  asdjshd +977-9841585917 +01-565859 asdksjad asdjshd +977-9841585917 +01-565859 asdksjad asdjshd +977-9841585917 +01-565859 asdksjad asdjshd +977-9841585917 +01-565859 asdksjad asdjshd +977-9841585917 +01-565859 asdksjad '
print(re.findall(pattern,sequence))
