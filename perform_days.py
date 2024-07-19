def weekday_1():
    import pandas as pd
    weekmask = 'Tue Wed Thu Fri'
    custombday = pd.offsets.CustomBusinessDay(weekmask=weekmask)
    e = pd.bdate_range('20250521','20250615', freq=custombday)
    #bdate_range 6
    #date_range 8
    print (e)
    minutes1 = len(e)
    print(minutes1)
    weekmask = 'Sat Sun'
    custombday = pd.offsets.CustomBusinessDay(weekmask=weekmask)
    e = pd.bdate_range('20250521','20250615', freq=custombday)
    print (e)
    minutes2 = len(e)
    print(minutes2)
    print("Shows: %d" % (minutes1 + 2*minutes2))


weekday_1()
