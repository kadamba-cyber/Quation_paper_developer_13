#	Question Paper Generation Project
import random
import openpyxl
import docx

#from openpyxl.styles import Alignment
doc = docx.Document()

path='D:/my docs/My Projects/exam quation_paper_developer/13/'                   #input excel File name

wb1=openpyxl.load_workbook(path+"13_input.xlsx",data_only=True)
sh1=wb1["INPSheet"]

            

#l1=[]                               #appending su_code for which q_papers are needed
for i in range(2,sh1.max_row+1):
    #l1.append(sh1.cell(i,2).value)
    sh2=wb1[sh1.cell(i,2).value]
    qb={1:[],2:[],3:[],4:[]}
    for j in range(2,sh2.max_row+1):
        l=[]
        l.append(sh2.cell(j,2).value)
        l.append(sh2.cell(j,3).value)
        l.append(sh2.cell(j,4).value)
        l.append(sh2.cell(j,5).value)
        qb[int(sh2.cell(j,6).value)].append(l)
    #print(qb)
    for k in qb:                                                        #hear k in unit number
        #print(qb[k],"\n")
        #print(k)
        main_q=[]
        total_marks=0                                                   #for setting 20 marks per quations
        while total_marks != 20:                                         # stoping the loop while 1 main quation is seted for 20 marks
            y=(random.randint(0,len(qb[k])-1))
            #print(y)
            y1=qb[k]
            if y1[y] not in main_q:
                if (total_marks+y1[y][1]) <= 20:
                    #print(y1[y],"\n")
                    y=(random.randint(0,len(qb[k])-1))
                    
                    if (20-(total_marks+y1[y][1])) >= 5 or total_marks+y1[y][1]==20 or (20-(total_marks+y1[y][1])) >= 9:
                        #print("a")
                        #print(y)
                        #print(y1[y])
                        #print(i)
                        total_marks+=y1[y][1]
                        main_q.append(y1[y])
                        #print(total_marks)
                    else:
                        #print("b")
                        #print(y)
                        #print(y1[y])
                        #print(total_marks)
                        pass
                else:
                    #print(y)
                    pass
            else:
                pass
           # print(total_marks)
        #print(k)
        print(main_q)
            