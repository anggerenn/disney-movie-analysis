from datetime import datetime

'''
"December 25, 1957"
"October 20, 1995  (U.S.)"
'''
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# months = r"January|February|March|April|May|June|July|August|September|October|November|December"

# dates = rf"({months})\s*\d*\,\s\d{4}"

# print(re.search(dates, "December 25, 1957"))

meh = "December 25, 1957"
frmt = "%B %d, %Y"
bro = datetime.strptime(meh,frmt)
print(bro)