import tkinter as tk
i=1
discount=0

root=tk.Tk()
root.configure(background="aqua")
root.geometry('1000x1200')
root.title("Naveen Restaurant")
#Table part
tablecheck=tk.Button(root,text="Check for available tables",font=("arial",18),command=lambda:checktable())
tablecheck.pack(pady=8,padx=20)

showtable=tk.Label(root,bg="aqua",fg="purple",font=("arial",18),text="")
showtable.pack(pady=8,padx=10)

# Menu Part
label1=tk.Label(root,text="Menu",bg="light green",font=("arial",28))
label1.pack(padx=10,pady=8)
label2=tk.Label(root,bg="light green",text="Aloo Paratha  Rs. 30")
label2.pack()
label3=tk.Label(root,bg="light green",text="Samosa  Rs. 15")
label3.pack()
label4=tk.Label(root,bg="light green",text="Pizza  Rs. 150")
label4.pack()
label5=tk.Label(root,bg="light green",text="Gulab Jamun  Rs. 35")
label5.pack()
label6=tk.Label(root,bg="light green",text="Chowmein  Rs. 70")
label6.pack()
label7=tk.Label(root,bg="light green",text="Churma  Rs. 200")
label7.pack()
#bill and order part
asking=tk.Label(root,text="Select your order",font=("ariale",18))
asking.pack(pady=10)

aloo=tk.Label(root,text="Aloo Paratha",font=("ariale",18))
aloo.pack(padx=30)
entry1=tk.Entry(root)
entry1.pack(pady=5)
samosa=tk.Label(root,text="Samosa",font=("ariale",18))
samosa.pack()
entry2=tk.Entry(root)
entry2.pack(pady=5)
pizza=tk.Label(root,text="Pizza",font=("ariale",18))
pizza.pack()
entry3=tk.Entry(root)
entry3.pack(pady=5)
gulab=tk.Label(root,text="Gulab Jamun",font=("ariale",18))
gulab.pack()
entry4=tk.Entry(root)
entry4.pack(pady=5)
chowmein=tk.Label(root,text="Chowmein",font=("arial",18))
chowmein.pack()
entry5=tk.Entry(root)
entry5.pack(pady=5)
churma=tk.Label(root,text="Churma",font=("ariale",18))
churma.pack()
entry6=tk.Entry(root)
entry6.pack(pady=5)
# bill=tk.Button(root,text="Get Bill",font=("arial",18),command=lambda:get_bill())
# bill.pack()
# billbtn=tk.Button(root,text="Get Bill",font=("arial",18),command=lambda:calculate())
# billbtn.pack()
# calculating bill
def calculate():
    
    dic={
        'aloo_paratha': [entry1,30],
        'samosa': [entry2,15],
        'pizza': [entry3,150],
        'gulab_jammun': [entry4,35],
        'chowmein': [entry5,70],
        'churma':[entry6,200]
        
    }
    global discount
    total=0
    net=0
    for key,val in dic.items():
        if(val[0].get()!=""):
            total=total+int(val[0].get())*val[1]
    if(total>=500):
        discount=5
    if(total>=1000):
        discount=10
    if(total<500):
        discount=1
    bill=tk.Label(root,text="Your total Bill Amount is : "+str(total)+" with "+str(discount)+"% discount",font=('arial',18))
    bill.pack()
    bill.after(1000,bill.destroy)
    net=total-(total*discount)/100
    billnet=tk.Label(root,text="You have to pay: "+str(net),font=('arial',18))
    billnet.pack()
    billnet.after(1000,billnet.destroy)

    root.after(1000,calculate)
    
def checktable():
    global i
    if(i<=20):
         
         showtable.config(text="Table no. "+str(i)+ " is available",bg="orange")
         
         i=i+1
         
    else:
        showtable.config(text="No Table is Available,Visit Again ☺",bg="red")
        exit(1)
        

root.after(3000,calculate)
root.mainloop()