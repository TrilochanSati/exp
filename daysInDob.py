from datetime import date



def daysInMonth(month:int,year:int)->int:
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(year%4==0 and month==2):
        return 29
    else:
        month-=1
        return months[month]

def daysInDob(dobDay,dobMonth,dobYear)->int:
    today=date.today()

    totalDays=0

    curDay=today.day
    curMonth=today.month
    curYear=today.year

    day=dobDay
    month=dobMonth
    year=dobYear

    while(day!=curDay or month!=curMonth or year!=curYear):


        dim=daysInMonth(month,year)
        if(day==dim):
            day=0
            month+=1

        totalDays+=1
        day+=1
        if(month>12):
            month=1
            year+=1
        print(day,month,year)
       
    return totalDays

print("days",daysInDob(27,9,2018))