''' 


THIS CODE GOOD!!!!!


'''


import os       
"""Fuctions"""      
clear=lambda:os.system("cls")                           #Clear_Fn
color_brwhite=lambda:os.system("color 0f")              #Default    #Bright_White_Color_Fn
color_green=lambda:os.system("color 0a")                #Success    #LiGreen_Color_Fn
color_red=lambda:os.system("color 0c")                  #Errors     #Red_Color_Fn
def mdy(d,y):                                           #To_Print_Day&Year  
    color_green()                                            
    print(day,end="")
    print(",",y)
def date_error():                                       #To_Print_Error
    color_red()                         
    print("Invalid Input, Date Cannot Be ",end='')
    print("'",end="")
    print(day,end="")

"""main"""
clear()                                         
color_brwhite()     
error,date1=0,""                            
date=list(input("Enter date In Format 'MM/DD/YYYY' : "))
if len(date)!=10:                                       #Length_Of_Date_Error
    color_red()                                 
    print("Error In Date, It Must Be Length Of '10' Including Slash Not With Length",end='')
    print("'",end="")
    print(len(date),end="")
    print("'")
else:
    month,day,year=date[0]+date[1],date[3]+date[4],date[6]+date[7]+date[8]+date[9]
    for i in range(9):                                  #List_To_Str
        date1+=date[i]
    for i in range(9):                                  #Error_In_Dates_Post
        if i!=2 and i!=5:
            if date[i].isnumeric()==False:
                color_red()
                print("Incorrect Date < '",date[i],"' Must Not Present In Date :",date1,"> At Postion :",i+1)
                error+=1
        else:
            if date[i]=='/':                            
                continue        
            else:
                print("Incorrect Date < ' / ' Must Present In Date At Correct Position> That Is :",i+1)
    if error==0:    
        if int(month)>12 or int(month)<=0:              #Month_Error
            color_red()                                 
            print("Invalid Input, Month Cannot Be,",end='')
            print("'",end="")
            print(month,end="")
            print("'")
        elif int(day)>31 or int(day)<=0:                #Date_Range_Error
            date_error()
            print("'")
        elif int(year)<=0:                              #Year_Error
            color_red()                                 
            print("Invalid Input, Year Cannot Be,",end='')
            print("'",end="")
            print(year,end="")
            print("'")
        elif month=='01':                               #Jan
            print("January ",end="")
            mdy(day,year)
        elif month=='02':                               #Feb
            if (int(year) % 400 == 0) or (int(year) % 100 != 0 and int(year) %4 == 0):
                if int(day)>29:                             #Leap_Year
                    date_error()
                    print("' In February Month")
                else :
                    print("February ",end="")
                    mdy(day,year)
            else :
                if int(day)>28:                             #Normal_Year
                    date_error()
                    print("' In February Month")
                else :
                    print("February ",end="")
                    mdy(day,year)
        elif month=='03':                               #March
            print("March ",end="")
            mdy(day,year)
        elif month=='04':                               #April
            if int(day)==31:
                date_error()
                print("' In April Month")
            else :
                print("April ",end="")
                mdy(day,year)
        elif month=='05':                               #May
            color_green()                                        
            print("May ",end="")
            mdy(day,year)
        elif month=='06':                               #June
            if int(day)==31:
                date_error()
                print("' In June Month")
            else :
                print("June ",end="")
                mdy(day,year)
        elif month=='07':                               #July
            print("July ",end="")
            mdy(day,year)
        elif month=='08':                               #Aug
            print("August ",end="")
            mdy(day,year)
        elif month=='09':                               #Sept
            if int(day)==31:
                date_error()
                print("' In September Month")
            else :
                print("September ",end="")
                mdy(day,year)
        elif month=='10':                               #Oct
            print("October ",end="")
            mdy(day,year)
        elif month=='11':                               #Nov
            if int(day)==31:
                date_error()
                print("' In November Month")
            else :
                print("November ",end="")
                mdy(day,year)
        elif month=='12':                               #Dec
            print("December ",end="")
            mdy(day,year)
input("\nHit Enter To Exit")                            #Console_Exit_Pause
