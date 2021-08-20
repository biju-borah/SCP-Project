def add_time(time, duration, day=""):
    showday = False
    days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    if len(day) != 0:
        showday = True
        for i in range(0,7):
            if days[i] == day.lower():
                index = i 
    if "AM" in time:
        T1 = "AM"
        start = time.split("AM")[0]
    else:
        T1 = "PM"
        start = time.split("PM")[0]
    start_time = start.split(":")
    h1 = int(start_time[0])
    m1 = int(start_time[1]) 
    cal_time = duration.split(":")
    h2 = int(cal_time[0])
    m2 = int(cal_time[1]) 
    flag1 = 0
    flag2 = 0
    for i in range(1,m2+1):
        if m1 == 59:
            flag2 += 1
            m1 = 0
        m1 += 1
    h2 += flag2
    for i in range(1,h2+1):
        if h1 == 12:
            flag1 += 1
            h1 = 0
        h1 += 1
    if T1 == "AM":
        temp = flag1//2
    else:
        if flag1%2 == 0:
            temp = flag1//2
        else:
            temp = flag1//2 + 1
    if flag1>1 and flag1%2 !=0:
        if T1 == "AM":
            T1 = "PM"
        else:
            T1 = "AM"
    elif flag1==1:
        if T1 == "AM":
            T1 = "PM"
        else:
            T1 = "AM"
    if showday:
        flag = 0
        for i in range(0,temp):
            flag += 1
            if(index == 7):
                index = 0
            index += 1
        if flag == 0:
            print(h1,m1,T1,days[index])
        else:
            if flag == 1:
                print(h1,m1,T1,days[index],"(Next Day)")
            else:
                print(h1,m1,T1,days[index],flag,"Days later")
    else:
        flag = 0
        for i in range(0,temp):
            flag += 1
        if flag == 1:
            print(h1,m1,T1,"(Next Day)")
        else:
            print(h1,m1,T1,flag,"Days later")


if __name__=="__main__":
    add_time("3:00 AM","24:30","monday")
