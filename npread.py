# -*-coding:utf-8-*-

import numpy

# str = np.loadtxt('intrinsics_depth.txt', delimiter=' ')
#
# print(str)
# nump1=[]
# nump2=[]

def txt_read(path):
    nump1=[]
    nump2=[]
    with open(path, "r", encoding="utf-8") as f_r:
        lines = f_r.readlines()
        #print(lines)
        k = 0
        for line in lines:

            #print(line)
            i = 0
            flag1 = 0
            flag = 0
            buff = ''
            nump1 = []
            for every_char in line:
                if every_char != ' ':
                    flag1 = 1
                    buff = buff + every_char
                if every_char == ' ':
                    flag = 1
                    if flag1 == 1:
                        nump1.append(float(buff))
                        i = i + 1
                        buff = ''
            k = 0
            nump2.append(nump1)


        f_r.close()

    nump3=numpy.array(nump2)
    #print(nump2)
    return nump3



