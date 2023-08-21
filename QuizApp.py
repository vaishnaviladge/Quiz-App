from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import mysql.connector as mysql
import time

def des():
    global back, lb
    imagel.destroy()
    btnn.destroy()
    lbl.destroy()
    question.destroy()
    option1.destroy()
    option2.destroy()
    option3.destroy()
    next_b.destroy()

counter=16
def time1():
        global lbl, counter 
        counter = counter-1
        if counter==0:
                lbl.config(text="upps!!Times UP",fg="red")
                score1()
                return
        else:
                lbl.config(text="00:"+str(counter))
                lbl.after(1000,time1)
             




# C/C++
Score = 0
Total_No_Questions = 5
Question_no = 1
Questions = ["Designer of C++ programming language.",
             "What is the only function all C programs must contain?",
             "Which of the following is not a correct variable type?",
             "Which of the following is the proper declaration of a pointer?",
             "Which of the following is the proper keyword to allocate memory?"]
Options = [["Charles Babbage", "Dennis Ritchie", "Bjarne Stroustrup"],
           ["start()", "main()", "Sstem()"],
           ["float", "int", "real"],
           ["int x;","int &x"," int *x"],
           ["malloc","new","create"]]

Answers = [3, 2, 3,3,2]

def remove():
        global l,b,b1,b2,b3,b4,b5
        l.destroy()
        b.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        c()
def c():
        
               
    global val1,val2,val3,lbl
    global question,option1,option2,option3,next_b,score,btnn,imagel
    question = Label(root, width=60,  bg="#003B46",fg="yellow",font=("Arial", 20),borderwidth=4 , relief="ridge", text=str(Question_no)+". "+Questions[0])
    question.place(x=220,y=150)

    val1 = IntVar()
    val2 = IntVar()
    val3 = IntVar()

    option1 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val1, text=Options[0][0], command=lambda: check(1))
    option1.place(x=600,y=250)

    option2 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val2, text=Options[0][1], command=lambda: check(2))
    option2.place(x=600,y=300)

    option3 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val3, text=Options[0][2], command=lambda: check(3))
    option3.place(x=600,y=350)

    next_b = Button(root, text="next ➤", bg="#F1F3CE",fg="black", font=("Arial", 17),command=next)
    next_b.place(x=650,y=430)
    imagel=Label(root,text="🤔",bg="#003B46",fg="yellow", font=("Arial", 40))
    imagel.place(x=670,y=480)

    btnn=Button(root,text="start timer",command=time1,bg="#F1F3CE",fg="black", font=("Arial", 15))
    btnn.grid(row=2,column=0)
    lbl=Label(root,text="00:",bg="#003B46",fg="White",font=("Arial", 23))
    lbl.grid(row=2,column=1)
    
        
    score = Label(root)
    score.place_forget()

def next():
    global val1,val2,val3,btnn,lbl
    global Score, Question_no,imagel
    global question,option1,option2,option3,next_b,score,back,lb,lt
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers[Question_no-1] == selected_option :
        Score += 1
        
        
    Question_no += 1
    if Question_no > Total_No_Questions:
        score1()
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=str(Question_no)+". "+Questions[Question_no-1])
        option1.config(text=Options[Question_no-1][0])
        option2.config(text=Options[Question_no-1][1])
        option3.config(text=Options[Question_no-1][2])
    
def score1():
        
        des()
 
        lb=Label(root,text="Thank You For Playing!!!",bg="#003B46",fg="yellow",font=("Tw Cen MT",35))
        lb.place(x=550,y=250)

        score.place(x=650,y=320)
        score.config(text="Your Score is :"+str(Score)+"/5",bg="#003B46",fg="yellow",font=("Tw Cen MT",25))
        back=Button(root,text="Quit",fg="black",font="verdana 20 bold",bg="#98DBC6",command=Quit)
        back.place(x=710,y=410)

def Quit():  

    root.destroy()
    root.quit()



def time2():
        global lbl, counter 
        counter = counter-1
        if counter==0:
                lbl.config(text="upps!!Times UP",fg="red")
                score2()
                return
        else:
                lbl.config(text="00:"+str(counter))
                lbl.after(1000,time2)



# JAVA
Score1 = 0
Total_No_Questions1 = 5
Question_no1 = 1

Questions1 = ["Who invented Java Programming?.",
             "Which statement is true about Java?",
             "Which component is used to compile, debug and execute the java programs?",
              "Which one of the following is not a Java feature?",
             "Which of these cannot be used for a variable name in Java?"]

Options1 = [["Guido van Rossum"," James Gosling"," Dennis Ritchie"],
           ["Java is a code dependent programming language","Java is a platform-dependent programming language"," Java is a platform-independent programming language"],
           ["JRE", "JDK"," JVM"],
           ["Object-oriented"," Use of pointers","Portable"],
           ["identifier & keyword"," identifier","keyword"]]
Answers1 = [2,3,2,2,3]

def remove1():
        global l,b,b1,b2,b3,b4,b5
        l.destroy()
        b.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        java()
def java():
    global val1,val2,val3
    global question,option1,option2,option3,next_b,score1,back3,btnn,lbl,imagel
    question = Label(root, width=60, bg="#003B46",fg="yellow",font=("Arial", 20),borderwidth=4 , relief="ridge", text=str(Question_no1)+". "+Questions1[0])
    question.place(x=220,y=150)

    val1 = IntVar()
    val2 = IntVar()
    val3 = IntVar()

    option1 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val1, text=Options1[0][0], command=lambda: check(1))
    option1.place(x=600,y=250)

    option2 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A",  variable=val2, text=Options1[0][1], command=lambda: check(2))
    option2.place(x=600,y=300)

    option3 = Checkbutton(root, bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val3, text=Options1[0][2], command=lambda: check(3))
    option3.place(x=600,y=350)

    next_b = Button(root, text=" Next ➤",bg="#F1F3CE",fg="black", font=("Arial", 17),command=next1)
    next_b.place(x=650,y=430)
    imagel=Label(root,text="🤔",bg="#003B46",fg="yellow", font=("Arial", 40))
    imagel.place(x=670,y=480)
    
    btnn=Button(root,text="start timer",command=time2,bg="#F1F3CE",fg="black", font=("Arial", 15))
    btnn.grid(row=2,column=0)
    lbl=Label(root,text="00:",bg="#003B46",fg="White",font=("Arial", 23))
    lbl.grid(row=2,column=1)

    score1 = Label(root)
    score1.place_forget()
def next1():
    global val1,val2,val3
    global Score1, Question_no1,imagel
    global question,option1,option2,option3,next_b,score1,back3,lb1,btnn
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers1[Question_no1-1] == selected_option :
        Score1 += 1

    Question_no1 += 1

    if Question_no1 > Total_No_Questions1:
            
        score2()
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=str(Question_no1)+". "+Questions1[Question_no1-1])
        option1.config(text=Options1[Question_no1-1][0])
        option2.config(text=Options1[Question_no1-1][1])
        option3.config(text=Options1[Question_no1-1][2])

def score2():
        des()
        lb1=Label(root,text="Thank You For Playing!!!",bg="#003B46",fg="yellow",font=("Tw Cen MT",35))
        lb1.place(x=550,y=250)
        score1.place(x=650,y=320)
        score1.config(text="Your Score is:"+str(Score1)+"/5", bg="#003B46",fg="yellow",font=("Tw Cen MT",25))
        back3=Button(root,text="Quit",fg="black",font="verdana 20 bold",bg="#98DBC6",command=Quit1)
        back3.place(x=710,y=410)
        
def Quit1():  

    root.destroy()
    root.quit()
    
    
   

def time3():
        global lbl, counter 
        counter = counter-1
        if counter<=0:
                lbl.config(text="upps!!Times UP",fg="red")
                score3()
                return
        else:
                lbl.config(text="00:"+str(counter))
                lbl.after(1000,time3)



# PYTHON
Score2 = 0
Total_No_Questions2 = 5
Question_no2 = 1

Questions2 = ["Who developed Python Programming Language?",
             "Which type of Programming does Python support?",
             "Which of the following is the correct extension of the Python file?",
             "Which of the following is used to define a block of code in Python language?",
             "Which keyword is used for function in Python language?"]

Options2 = [["Wick van Rossum","Rasmus Lerdorf","Guido van Rossum"],
           ["object-oriented programming"," structured programming","Both"],
           [".python",".pl"," .py"],
           ["Indentation"," Key","Brackets"],
           ["Function"," Def"," Fun"]]
Answers2 = [3,3,3,1,2]

def remove2():
        global l,b,b1,b2,b3,b4,b5
        l.destroy()
        b.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        python()

def python():
    global val1,val2,val3
    global question,option1,option2,option3,next_b,score2,back,lbl,btnn,imagel
    question = Label(root, width=60, bg="#003B46",fg="yellow",font=("Arial", 20), borderwidth=4 , relief="ridge",text=str(Question_no2)+". "+Questions2[0])
    question.place(x=220,y=150)

    val1 = IntVar()
    val2 = IntVar()
    val3 = IntVar()

    option1 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val1, text=Options2[0][0], command=lambda: check(1))
    option1.place(x=600,y=250)

    option2 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val2, text=Options2[0][1], command=lambda: check(2))
    option2.place(x=600,y=300)

    option3 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A",variable=val3, text=Options2[0][2], command=lambda: check(3))
    option3.place(x=600,y=350)

    next_b = Button(root, text="next ➤",bg="#F1F3CE",fg="black", font=("Arial", 17), command=next2)
    next_b.place(x=650,y=430)
    imagel=Label(root,text="🤔",bg="#003B46",fg="yellow", font=("Arial", 40))
    imagel.place(x=670,y=480)

    btnn=Button(root,text="start timer",command=time3,bg="#F1F3CE",fg="black", font=("Arial", 15))
    btnn.grid(row=2,column=0)
    lbl=Label(root,text="00:",bg="#003B46",fg="White",font=("Arial", 23))
    lbl.grid(row=2,column=1)

    score2 = Label(root)
    score2.place_forget()

def next2():
    global val1,val2,val3
    global Score2, Question_no2,imagel
    global question,option1,option2,option3,next_b,score2,back4,lb2
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers2[Question_no2-1] == selected_option :
        Score2 += 1

    Question_no2 += 1

    if Question_no2 > Total_No_Questions2:
        score3()
        
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=str(Question_no2)+". "+Questions2[Question_no2-1])
        option1.config(text=Options2[Question_no2-1][0])
        option2.config(text=Options2[Question_no2-1][1])
        option3.config(text=Options2[Question_no2-1][2])

def score3():
        des()
        lb2=Label(root,text="Thank You For Playing!!!",bg="#003B46",fg="yellow",font=("Tw Cen MT",35))
        lb2.place(x=550,y=250)
        score2.place(x=650,y=320)
        score2.config(text="Your Score is:"+str(Score2)+"/5",bg="#003B46",fg="yellow",font=("Tw Cen MT",25))
        back4=Button(root,text="Quit",fg="black",font="verdana 20 bold",bg="#98DBC6",command=Quit2)
        back4.place(x=710,y=410)
        
def Quit2():  

    root.destroy()
    root.quit()

    
def time4():
        global lbl, counter 
        counter = counter-1
        if counter<=0:
                lbl.config(text="upps!!Times UP",fg="red")
                score4()
                return
        else:
                lbl.config(text="00:"+str(counter))
                lbl.after(1000,time4)


#javascript
Score3 = 0
Total_No_Questions3 = 5
Question_no3 = 1
        
Questions3 = ["Which one of the following is the correct way for calling the JavaScript code?",
             "Which of the following is correct about JavaScript?",
             "Arrays in JavaScript are defined by which of the following statements?",
             "Where is Client-side JavaScript code is embedded within HTML documents?",
             "What is the basic difference between JavaScript and Java?"]

Options3 = [["Preprocessor","Triggering Event","Function/Method"],
            ["JavaScript is an Object-Based language"," JavaScript is Assembly-language","JavaScript is an Object-Oriented language"],
           ["It is an ordered list of values","It is an ordered list of objects"," It is an ordered list of string"],
           ["A URL that uses the special javascript:code"," A URL that uses the special javascript:protocol","A URL that uses the special javascript:encoding"],
           ["Functions are considered as fields","Functions are values, and there is no hard distinction between methods and fields","Variables are specificn"]]
Answers3 = [3,1,1,2,2]

def remove3():
        global l,b,b1,b2,b3,b4,b5
        l.destroy()
        b.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        jscript()

def jscript():
    global val1,val2,val3
    global question,option1,option2,option3,next_b,score3,lbl,btnn,imagel
    question = Label(root, width=60, bg="#003B46",fg="yellow",font=("Arial", 20),borderwidth=4 , relief="ridge", text=str(Question_no3)+". "+Questions3[0])
    question.place(x=220,y=150)

    val1 = IntVar()
    val2 = IntVar()
    val3 = IntVar()

    option1 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A",variable=val1, text=Options3[0][0], command=lambda: check(1))
    option1.place(x=600,y=250)

    option2 = Checkbutton(root, bg="#003B46",font=("Arial", 17),fg="#D9B44A",variable=val2, text=Options3[0][1], command=lambda: check(2))
    option2.place(x=600,y=300)

    option3 = Checkbutton(root, bg="#003B46",font=("Arial", 17),fg="#D9B44A",variable=val3, text=Options3[0][2], command=lambda: check(3))
    option3.place(x=600,y=350)

    next_b = Button(root, text="next ➤",bg="#F1F3CE",fg="black", font=("Arial", 17), command=next3)
    next_b.place(x=650,y=430)
    imagel=Label(root,text="🤔",bg="#003B46",fg="yellow", font=("Arial", 40))
    imagel.place(x=670,y=480)

    btnn=Button(root,text="start timer",command=time4,bg="#F1F3CE",fg="black", font=("Arial", 15))
    btnn.grid(row=2,column=0)
    lbl=Label(root,text="00:",bg="#003B46",fg="White",font=("Arial", 23))
    lbl.grid(row=2,column=1)

    score3 = Label(root)
    score3.place_forget()

def next3():
    global val1,val2,val3
    global Score3, Question_no3,back5,imagel
    global question,option1,option2,option3,next_b,score3,lb3
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers3[Question_no3-1] == selected_option :
        Score3 += 1
        
    Question_no3 += 1

    if Question_no3 > Total_No_Questions3:
        score4()
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=str(Question_no3)+". "+Questions3[Question_no3-1])
        option1.config(text=Options3[Question_no3-1][0])
        option2.config(text=Options3[Question_no3-1][1])
        option3.config(text=Options3[Question_no3-1][2])

def score4():
        des()
        lb3=Label(root,text="Thank You For Playing!!!",bg="#003B46",fg="yellow",font=("Tw Cen MT",35))
        lb3.place(x=550,y=250)
        score3.place(x=650,y=320)
        score3.config(text="Your Score is:"+str(Score3)+"/5",bg="#003B46",fg="yellow",font=("Tw Cen MT",25))
        back5=Button(root,text="Quit",fg="black",font="verdana 16 bold",bg="#98DBC6",command=Quit3)
        back5.place(x=710,y=410)
        
def Quit3():  
    root.destroy()
    root.quit()
def time5():
        global lbl, counter 
        counter = counter-1
        if counter<=0:
                lbl.config(text="upps!!Times UP",fg="red")
                score5()
                return
        else:
                lbl.config(text="00:"+str(counter))
                lbl.after(1000,time5)


        
#MYSQL
Score4 = 0
Total_No_Questions4 = 5
Question_no4 = 1


Questions4 = ["Which type of database management system is MySQL?",
             "What is data in a MySQL database organized into?",
             "What represents an ‘attribute’ in a relational database?",
             "What represents a ‘tuple’ in a relational database?",
             "Which is the MySQL instance responsible for data processing?"]

Options4 = [["Object-oriented"," Hierarchical"," Relational"],
             ["Objects"," Tables"," Networks"],
            ["Table", "Row" ,"Column"],
           ["Table","Row"," Column"],
           ["A URL that uses the special javascript:code"," A URL that uses the special javascript:protocol","A URL that uses the special javascript:encoding"],
           ["MySQL client","MySQL server","SQL"]]
Answers4 = [3,2,3,2,2]

def remove4():
        global l,b,b1,b2,b3,b4,b5
        l.destroy()
        b.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        msql()

def msql():
    global val1,val2,val3
    global question,option1,option2,option3,next_b,score4,lbl,btnn,imagel
    question = Label(root, width=60, bg="#003B46",fg="yellow",font=("Arial", 20), borderwidth=4 , relief="ridge", text=str(Question_no4)+". "+Questions4[0])
    question.place(x=220,y=150)

    val1 = IntVar()
    val2 = IntVar()
    val3 = IntVar()

    option1 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val1, text=Options4[0][0], command=lambda: check(1))
    option1.place(x=600,y=250)

    option2 = Checkbutton(root, bg="#003B46",font=("Arial", 17),fg="#D9B44A",variable=val2, text=Options4[0][1], command=lambda: check(2))
    option2.place(x=600,y=300)
    option3 = Checkbutton(root,bg="#003B46",font=("Arial", 17),fg="#D9B44A", variable=val3, text=Options4[0][2], command=lambda: check(3))
    option3.place(x=600,y=350)

    next_b = Button(root, text="next ➤",bg="#F1F3CE",fg="black", font=("Arial", 17), command=next4)
    next_b.place(x=650,y=430)

    imagel=Label(root,text="🤔",bg="#003B46",fg="yellow", font=("Arial", 40))
    imagel.place(x=670,y=480)

    btnn=Button(root,text="start timer",command=time5,bg="#F1F3CE",fg="black", font=("Arial", 15))
    btnn.grid(row=2,column=0)
    lbl=Label(root,text="00:",bg="#003B46",fg="White",font=("Arial", 23))
    lbl.grid(row=2,column=1)
    
    score4 = Label(root)
    score4.place_forget()

def next4():
    global val1,val2,val3
    global Score4, Question_no4,imagel
    global question,option1,option2,option3,next_b,score4,back6,lb4
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers4[Question_no4-1] == selected_option :
        Score4 += 1

    Question_no4 += 1

    if Question_no4 > Total_No_Questions4:
        score5()
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=str(Question_no4)+". "+Questions4[Question_no4-1])
        option1.config(text=Options4[Question_no4-1][0])
        option2.config(text=Options4[Question_no4-1][1])
        option3.config(text=Options4[Question_no4-1][2])

def score5():
    
        des()
        lb4=Label(root,text="Thank You For Playing!!!",bg="#003B46",fg="yellow",font=("Tw Cen MT",35))
        lb4.place(x=550,y=250)
        score4.place(x=650,y=320)
        score4.config(text="Your Score is:"+str(Score4)+"/5", bg="#003B46",fg="yellow",font=("Tw Cen MT",25))
        back6=Button(root,text="Quit",fg="black",font="verdana 20 bold",bg="#98DBC6",command=Quit4)
        back6.place(x=710,y=410)
        
def Quit4():  

    root.destroy()
    root.quit()


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


def back1():
    global l,b,b1,b2,b3,b4,b5
    l.destroy()
    b.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    login()
    
       
def welcome():
        
           
    global l,b,b1,b2,b3,b4,b5
    l=Label(root,text="*** Welcome To The Programming Quiz Test ***",fg="#ccff80",bg="#003B46",font=("Kristen ITC",40,"bold"))
    l.place(x=200,y=210)


    b=Button(root,text="©  C/C++  ",font="bold 20",bg="#CD8C8C",command=remove)
    b.place(x=530,y=350)

    b1=Button(root,text="♨  Java  ",font="bold 20",bg="#D4B8B1",command=remove1)
    b1.place(x=750,y=350)

    b2=Button(root,text="≛ Python  ",font="bold 20",bg="#D4B8B1",command=remove2)
    b2.place(x=640,y=450)
    
    b3=Button(root,text="⌨  Javascript  ",font="bold 20",bg="#D4B8B1",command=remove3)
    b3.place(x=840,y=450)

    b4=Button(root,text="⌸ Mysql  ",font="bold 20",bg="#CD8C8C",command=remove4)
    b4.place(x=960,y=350)
    b5=Button(root,text="⇦ Back",fg="black",font="verdana 16 bold",bg="#98DBC6",command=back1)
    b5.place(x=760,y=650)

    


def confirm():
    global l,l2,l3,l4,l5,l6,l1
    global e1,e2,e3,e4
    global e5,e6,b1
    l.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()      
    l5.destroy() 
    l6.destroy()
    e1.destroy()
    e2.destroy()      
    e3.destroy()
    e4.destroy()
    e5.destroy()
    e6.destroy()
    b1.destroy()
    b2.destroy()
    login()
def open_window():

    def check():

      name =Entry.get(e1)
      roll =Entry.get(e2)
      mail =Entry.get(e3)
      unm =Entry.get(e4)
      password =Entry.get(e5)
      cpass =Entry.get(e6)

      if(name!="" and roll!="" and mail!="" and password!="" and cpass!=""):
        if (password!=cpass):
            messagebox.showinfo("Error,Password doesn't match")
        else:
            con= mysql.connect(host="localhost",user="root",password="",database="quiz")

            cursor=con.cursor()
            cursor.execute("insert into users values('"+name+"','"+roll+"','"+mail+"','"+unm+"','"+password+"','"+cpass+"')")
            cursor.execute("commit")

            messagebox.showinfo("signUp status","Signup successful!!!!")

            con.close()
            x=confirm()
      else:
            messagebox.showinfo("Error","please fill all the fields")
            
    global l,l1,l2,l3,l4,l5,l6,e1,e2,e3,e4,e5,e6,b1,b2
    l=Label(root,text="SignUp!!",fg="black",bg="#F1F3CE",font=("Lucida Handwriting",25,"bold"))
    l.place(x=620,y=100)

    l1=Label(root,text="Name :",bg="#003B46",fg="#F1F3CE",font="verdana 20 bold")
    l1.place(x=500,y=200)
    e1=Entry(root,bg="#C4DFE6",width=25,bd=3)
    e1.place(x=800,y=210)

    l2=Label(root,text="Enrollment No:",bg="#003B46",fg="#F1F3CE",font="verdana 20 bold")
    l2.place(x=500,y=250)
    e2=Entry(root,bg="#C4DFE6",width=25,bd=3)
    e2.place(x=800,y=260)

    l3=Label(root,text="Email:",bg="#003B46",fg="#F1F3CE",font="verdana 20 bold")
    l3.place(x=500,y=300)
    e3=Entry(root,bg="#C4DFE6",width=25,bd=3)
    e3.place(x=800,y=310)
 
    l4=Label(root,text="Enter Username:",bg="#003B46",fg="#F1F3CE",font="verdana 20 bold")
    l4.place(x=500,y=350)
    e4=Entry(root,bg="#C4DFE6",width=25,bd=3)
    e4.place(x=800,y=360)

    l5=Label(root,text="Enter Password:",bg="#003B46",fg="#F1F3CE",font="verdana 20 bold")
    l5.place(x=500,y=400)
    e5=Entry(root,bg="#C4DFE6",width=25,bd=3)
    e5.place(x=800,y=410)

    l6=Label(root,text="Confirm Password:",bg="#003B46",fg="#F1F3CE",font="verdana 20 bold")
    l6.place(x=500,y=450)
    e6=Entry(root,bg="#C4DFE6",width=25,bd=3)
    e6.place(x=800,y=460)

    b1=Button(root,text="Submit",fg="black",font="verdana 20 bold",bg="#98DBC6",command=check)
    b1.place(x=750,y=550)
    b2=Button(root,text="⇦ Back",fg="black",font="verdana 20 bold",bg="#98DBC6",command=confirm)
    b2.place(x=570,y=550)
   

def rem():
    global l1,l2,l0,e1,e2,b1,b2,fm
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    welcome()
def sigup():
    global l1,l2,l0,e1,e2,b1,b2,fm
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    open_window()

con=mysql.connect(host="localhost",user="root",password="",database="quiz")
cursor=con.cursor()

def user_login(uname,passw):
    try:
       cursor.execute("select * from `users` where `unm` ='"+uname+"' and `password`='"+passw+" '")
       return (cursor.fetchone())
    except:
        return sfalse
def msg():
    uname=Entry.get(e1)
    passw=Entry.get(e2)

    if(uname =="" or passw==""):
        messagebox.showinfo("Alert","Fill all details.......")
    else:
        res=user_login(uname,passw)
        if res:
            messagebox.showinfo("Message","Login Successfully....")
            x=rem()
        else:
             messagebox.showinfo("Alert","Login Failed....")



        
root=Tk()
root.title("Quiz Test")
root.geometry("1350x700+0+0")
root.config( bg="#003B46")
root.resizable()

def login():
    global l1,l2,l0,e1,e2,b1,b2,fm

    l0=Label(root,text="LOGIN!!!",bg="#F1F3CE",fg="black",font=("Lucida Handwriting",25,"bold"))
    l0.place(x=620,y=125)

    fm=Frame(root,bd=4,relief=RIDGE,bg="#66A5AD")
    fm.place(x=450,y=200,width=500,height=400)

    l1=Label(fm,text="Username:",bg="#66A5AD",font="verdana 20 bold")
    l1.grid(row=1,column=0,padx=20,pady=40)
    e1=Entry(fm,bg="#C4DFE6")
    e1.grid(row=1,column=1,padx=20)

    l2=Label(fm,text="Password:",bg="#66A5AD",font="verdana 20 bold")
    l2.grid(row=2,column=0,padx=20,pady=40)
    e2=Entry(fm,bg="#C4DFE6",show="x")
    e2.grid(row=2,column=1,padx=20)

    b1=Button(fm,text="Login",fg="black",font="verdana 16 bold",bg="#98DBC6",command=msg)
    b1.grid(row=3,column=0,padx=70,pady=20)

    b2=Button(fm,text="Sign Up",fg="black",font="verdana 16 bold",bg="#98DBC6",command=sigup)
    b2.grid(row=3,column=1,padx=70,pady=20)

login()   

root.mainloop()
