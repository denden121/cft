import argparse
from tempfile import TemporaryFile
#считыввание всех агрументов и флагов с консоли с проверкой
'''
def start_console():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",action="store_true")
    parser.add_argument("-i",action="store_true")
    parser.add_argument("-d",action="store_true")
    parser.add_argument("-a",action="store_true")
    parser.add_argument("output",type = str)
    parser.add_argument("input",type=str,nargs='*')
    args = parser.parse_args()
    if not(args.s) and not(args.i):
        print ("error1")
        exit()
    if args.s and args.i:
        print("error2")
        exit()
    if args.d and args.a:
        print("error3")
        exit()
    return args
'''
#режим сортировки
def mode_sort(sort_down):#-d
    if not(sort_down):
        return True # если нужно отсортировать по возрастанию
    return False#убыванию
#входные данные 
def date_sort(sort_integer,#-i
              sort_string):#-s
    if sort_integer:
        return True#если входные данные типа integer
    return False#string
def boolean(temp_a,temp_b,mode,date):
    if mode and date:#условие когда последовательность возрастает и тип int 
        if not(int(temp_a) <= int(temp_b)):
            return False
    elif mode and not(date):#условие когда последовательность возрастает и тип str
        if not(temp_a <= temp_b):
            return False
    elif not(mode) and date:#условие когда последовательность убывает и тип int
        if not(int(temp_a)> int(temp_b)):
            return False
    else:#условие когда последовательность убывает и тип str
        if not(temp_a > temp_b):
            return False
    return True
def flag(a,b,mode,date):
    if mode and date:#условие когда последовательность возрастает и тип int 
        if int(a) <= int(b):
            return a
        else: 
            return b
    elif mode and not(date):#условие когда последовательность возрастает и тип str
        if a <= b:
            print(a)
            return a
        else: 
            return b
    elif not(mode) and date:#условие когда последовательность убывает и тип int
        if int(a)> int(b):
            print(b)
            return a
        else: 
            return b
    else:#условие когда последовательность убывает и тип str
        if a > b:
            print(a)
            return a
        else: 
            return b

def check_file(file,date,mode):#функция для проверки файла на битость(что все элеменыт убывают или возрастают) и заранее узнать количество записей в файле
    temp_num=0 #для посчета количества записей файлов       
    temp_a = file.readline()
    temp_b = file.readline()
    temp_num +=2
    for line in file:
        if not(boolean(temp_a,temp_b,mode,date)):
            break
        temp_a = temp_b
        temp_b = line
        temp_num +=1
    if not(boolean(temp_a,temp_b,mode,date)):
        temp_num -=1
    return temp_num
def sort_file(first_file,second_line,output_temp ,mode,date,flag_file):
    if not(flag_file):
        first = open(first_file, 'r')
        num_first = check_file(first, mode, date)
        first.close()
    #print(num_first)
    second = open(second_line, 'r')
    num_second = check_file(second, mode, date)
    second.close()
    #print(num_second)
    ########################
    if not(flag_file):
        first = open(first_file, 'r')
    else:
        first = first_file
    second = open(second_line, 'r')
    a = first.readline()
    # num_first -=1
    b = second.readline()
    # num_second -=1
    while a != "" and b != "":
        out.write(flag(a, b, mode, date))
        if flag(a, b, mode, date) == a:
            a = first.readline()
        else:
            b = second.readline()
    print("a = {} b = {} ".format(a, b))
    if a == "":
        out.write(b)
        for i in second:
            out.write(i)
    elif b == "":
        print("a = {} b = {} ".format(a, b))
        out.write(a)
        for i in first:
            out.write(i)
    return out
####################################
'''
args = start_console()
mode = mode_sort(args.d)
date = date_sort(args.i,args.s)
'''
mode = False
date = True
argsinput = ['in1.txt','in2.txt','in3.txt','in4.txt']
argsoutput = 'out.txt'
print(date,mode)
if len(argsinput) == 2:
    out = open(argsoutput,'w+')
    file = sort_file(argsinput[0],argsinput[1],out,mode,date)
    file.close()
if len(argsinput) >2:
    out = TemporaryFile('w+')
    flag_file = False
    file = sort_file(argsinput[0], argsinput[1], out, mode, date,flag_file)
    file.seek(0)
    print(file)
    del (argsinput[0])
    del(argsinput[0])
    print(argsinput)
    while len(argsinput)!=1:
        out = TemporaryFile('w+')
        flag_file = True
        file_temp = sort_file(file, argsinput[0], out, mode, date, flag_file)
        file_temp.seek(0)
        del (argsinput[0])
        file = file_temp
    out = open(argsoutput,'w+')
    flag_file = True
    finish = sort_file(file,argsinput[0],out,mode,date,flag_file)



