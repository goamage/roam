def week(i):
    switcher={
            0:'Error',
            1:'Separator',
        }
    s2 = 'text'
    s3 = 'eeee'
    s4 = switcher.get(i,"Invalid day of week")
    #return switcher.get(i,"Invalid day of week")

    #print(switcher.get(i,"Invalid day of week"))

    return s2, s3, s4

#print(week(1))

res = week(0)

print(res[2])