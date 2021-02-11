#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime
import time
import os


class Customer(object):                           # Customer class, used to store the customer detail for future
    def __init__(self,name,table_no,number_of_sit,food_time,receipt):
        self.name=name
        self.table_no=table_no
        self.number_of_sit=number_of_sit
        self.food_time=food_time
        self.receipt_no=receipt
        self.reservation_time=datetime.now().strftime("%I:%M:%S %p")
        self.reservation_date=datetime.now().strftime("%d-%b-%Y")
    
    def show(self):
        print(f'*******Receipt No -> {self.receipt_no} *********')
        print(f'Name-> {self.name}')
        print(f'Table No-> {self.table_no}, Chairs Booked-> {self.number_of_sit}')
        print(f'Reservation for {self.food_time}')
        print(f'Reservation Time {self.reservation_time}')
        print(f'Reservation is valid {self.reservation_date}')
        print(f'------------------DONE----------------------')
class ReservationSystem:                             # class Reservation for all sits availablity details
    def __init__(self):
        self.total_table=5
        self.sits_available=[]
        
    def TableList(self,lists):         # Create a function to get all details about Table and sits..
                    
        location=sorted(lists,key=lists.get,reverse=True)         # location of each table 
                                                 
        for i in range(len(location)):                            # for loop for arranging the sits according to locations
            self.sits_available.append(lists[location[i]])
       
        for i in range(0,self.total_table):                            # Display all the table with updated sits availability...
            print(f'Table No {location[i]}, Sits Available {self.sits_available[i]}')
    
class Receipt:
    def __init__(self,n):
        self.n=n
    def receipt_no(self):
        for i in range(1,self.n):
            yield i 

if __name__=='__main__':
    
    customers_detail=[]
    food_time_dic={'1':'Breakfast 8 AM to 10AM','2':'Lunch 12 PM to 3 PM','3':'Dinner 7 PM to 11 PM'}  # use dict for asked for customer in which customer would to prefer
    list_breakfast={'1':4,'2':4,'3':4,'4':4,'5':4}                     # Dictionary of list of table and available sits....
    lists_lunch={'1':4,'2':4,'3':4,'4':4,'5':4}  
    lists_dinner={'1':4,'2':4,'3':4,'4':4,'5':4}
    super_list={'1':list_breakfast,'2':lists_lunch,'3':lists_dinner}
    receipt=Receipt(21)
    r=receipt.receipt_no()
    while True:
        print('******** Online Reservation System ********')
        print('1. Available Tables\n2. Reserve your sit\n3.Customer Booked details')
        ch=int(input())                                        # name value to get ans with customer..
        table_list=ReservationSystem()
        if ch==1:
            food_tim=input('1. BreadFast list\n2. Lunch List\n3. Dinner List')
            table_list.TableList(super_list[food_tim])                                   # call the TableList function to display the details.
            ans=input('Do you want to Reserve sits(Y/N):> ')   # Asked the customer , if he/she want to continue with us...
            if ans=='Y':
                os.system('cls')
                continue
            else:
                break
        elif ch==2:
            customer_name=input('Enter your name please:> ')   # Get customer name
            print()
            print(f'Welcome ,{customer_name}',sep="\n")
            print()
            food_time=input('1.Reserve for Breakfast\n2.Reserve for Lunch\n3.Reserve for Dinner  ')
            print()
            print('List of Tables and sit availability')       # Display table details
            time.sleep(2)
            lists=super_list[food_time]
            table_list.TableList(lists)
            time.sleep(1)
            print()
            table_no=input('In which table do you prefer to Reserve:> ')
            number_of_sits=int(input('How many sits you want to Reserve:> '))
            time_=datetime.now()
            print()
            time.sleep(1)
            if lists[table_no]-number_of_sits>=0:               # sits should not be less then zero after getting data..
                lists[table_no]=lists[table_no]-number_of_sits
                
                time.sleep(1)
                print()
                receipt=r.__next__()
                customers_detail.append(Customer(customer_name,table_no,number_of_sits,food_time_dic[food_time],receipt))
                print(f'********** **** RECEIPT {receipt} **** **************')   # Receipt detail of the customer
                print(f'Name-> {customer_name}')
                print(f'Table Number-> {table_no}, Number of sits-> {number_of_sits}')
                print(f'Your reservation is for, {food_time_dic[food_time]}')
                print(f'Reservation Time,{time_.strftime("%I:%M:%S %p")}')
                print(f'Your Reservation is valid,{time_.strftime("%d-%b-%Y")}')
                print('|-----------------SUCCESS------------------|')    # successful message 
            else:
                print(f'*********Sorry {lists[table_no]} chairs available***********')
                print('*You can choose other table instead of this*')
            
                
            
            ans=input('Do you want to Reserve more sits(Y/N):> ')     # Asked the customer , if he/she want to continue with us.
            if ans=='Y':
                os.system('cls')
                continue
            else:
                break
        elif ch==3:
            if len(customers_detail)==0:
                print('Booking List Empty')
            for c in customers_detail:
                c.show()
            ans=input('Do you want to Reserve sits(Y/N):> ')     # Asked the customer , if he/she want to continue with us.
            if ans=='Y':
                os.system('cls')
                continue
            else:
                break


# In[ ]:




