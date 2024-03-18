def main():
    nimi=input("Sisesta nimi: ")
    while True:
        date=input("Sisesta sünniaeg (d.m.y formaadis): ")
        if date.count('.')!=2:
            print("Vale formaat")
            continue
        day,month,year=date.split(".")
        if not (1<=len(day)<=2 and 1 <=len(month)<=2 and 1 <=len(year)<=4):
            print("Vale formaat")
            continue
        if not (1<=int(day)<=31 and 1 <=int(month)<=12 and 1<=int(year)<=2666):
            print("Vale kuupäev")
            continue
        break
    
    numbers=get_numbers(date)
    
    numbstring,formatted_data=format_data(numbers)
    
    print_result(nimi,formatted_data)
    
    salvesta_failis(nimi,date,numbstring)
    
    if input("Näidata tõlgendust (y/n) :")=="y":
        find_info(numbstring)
    
    if input("\nProovi uuesti? (y/n) :" )=="y":
        main()
    else:
        exit()
    
def get_numbers(date):
    day,month,year=date.split(".")
    daysum=monthsum=worknumber2=worknumber4=year_sum=0
    
    for i in range(len(day)): daysum+=int(day[i])
    for i in range(len(month)): monthsum+=int(month[i])
    for i in range(len(year)): year_sum+=int(year[i])
        
    worknumber1=daysum+monthsum+year_sum
        
    for i in range(len(str(worknumber1))): worknumber2+=int(str(worknumber1)[i])
        
    worknumber3=int(worknumber1)-2*(int(day[0]))

    for i in range(len(str(worknumber3))): worknumber4+=int(str(worknumber3)[i])
        
    numbers=day+month+year+str(worknumber1)+str(worknumber2)+str(worknumber3)+str(worknumber4)
    
    return numbers
    
def format_data(numbers):
    data=[]
    numberstring=""
    for i in range(1,10,3):
        count1=numbers.count(str(i))
        count2=numbers.count(str(i+1))
        count3=numbers.count(str(i+2))
        outs=str(i)*count1+" "+str(i+1)*count2+" "+str(i+2)*count3
        d=outs.split(" ")
        for i in range(len(d)):
            if not d[i]:
                d[i] = "-"
        outs="|".join(d)
        data.append(outs)
        datarow=",".join(outs.split("|"))
        datarow+=","
        numberstring+=datarow

    numberstring=numberstring[:-1]
    maxlen = 0
    for row in data:
        for num in row.split("|"):
            strip_num = num.strip()
            if len(strip_num) > maxlen:
                maxlen = len(strip_num)
    
    formatted_data = []
    for row in data:
        numb = row.split("|")
        format_num = []
        for num in numb:
            strip_num = num.strip()
            format_num.append(f"{strip_num:>{maxlen}}")
        
        format_row = "|"
        for num in format_num:
            format_row += f" {num} |"
        
        formatted_data.append(format_row)
        
    return numberstring,formatted_data
        
def print_result(nimi,formatted_data):
    print(f"\nTeie Pythagorase ruut, {nimi}:")
    print("_"*len(formatted_data[0]))
    for row in formatted_data:
        print(row)
    print("‾"*len(formatted_data[0]))
    
def salvesta_failis(nimi,date,numbrid):
    failname = "ruut_salvestatud_andmed.txt"
    f = open(failname,'a',encoding="utf-8")
    f.write(f"\nNimi: {nimi}, Sünnipäev: {date}, Numbrid: {numbrid}")
        
def find_info(numbstring):
    numblist=list(numbstring.split(","))
    failname = "Pythagoorase omaduste nimekiri.txt"
    f = open(failname,'r',encoding="utf-8")
    lines = f.readlines()
    found = []
    zeros=[]
    for index, char in enumerate(numblist):
         if char == "-":
            zeros.append(str(index+1) + ")")
    for line in lines:
        words = line.split(" ")
        for zero in zeros:
            if words[0] in zero and len(words[0])==len(zero):
                found.append(f"нет {zero[:-1]}"+lines[lines.index(line)+1][3:])
        for num in numblist:
            if words[0] in num and len(words[0])==len(num):
                found.append(line.strip())
    found = [f.replace("\n", "" ) for f in found]
    for f in found:
        print(f"\n{f}")
    
