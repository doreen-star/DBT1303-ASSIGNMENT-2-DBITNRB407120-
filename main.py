from tkinter import *
import time
import random
import tkinter.messagebox

root =Tk()
root.geometry("1400x750+0+0")
root.title("Restaurant Ordering System")
root.configure(background='sky blue')

Tops = Frame(root, bg='dark blue', bd=25, pady=20, relief=GROOVE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 40, 'bold'), text='HOTeli Restaurant', bd=15, bg='sky blue',
                fg='dark blue', justify=CENTER)
lblTitle.grid(row=0)



ReceiptCal_Function = Frame(root, bg='dark blue', bd=10, relief=GROOVE)
ReceiptCal_Function.pack(side=LEFT)

Buttons_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=3, relief=GROOVE)
Buttons_Function.pack(side=TOP)

Calculator_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=6, relief=GROOVE)
Calculator_Function.pack(side=BOTTOM)

Receipt_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=4, relief=GROOVE)
Receipt_Function.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='dark blue', bd=32, relief=GROOVE)
MenuFrame.pack(side=RIGHT)

Total_Function = Frame(MenuFrame, bg='sky blue', bd=4)
Total_Function.pack(side=BOTTOM)

Drinks_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Drinks_Function.pack(side=LEFT)

Food_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Food_Function.pack(side=RIGHT)

# Variables-----------------------------------------

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()

Date_of_Order = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Total_of_Food = StringVar()
Total_of_Drinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

cocktail = StringVar()
iced_tea = StringVar()
hot_chocolate = StringVar()
juice = StringVar()
milkshake = StringVar()
water = StringVar()
soda = StringVar()
coffee = StringVar()

fried_chicken = StringVar()
fried_beef = StringVar()
chips = StringVar()
ugali = StringVar()
githeri = StringVar()
mokimo = StringVar()
chapati = StringVar()
fish = StringVar()

cocktail.set("0")
iced_tea.set("0")
hot_chocolate.set("0")
juice.set("0")
milkshake.set("0")
water.set("0")
soda.set("0")
coffee.set("0")

fried_chicken.set("0")
fried_beef.set("0")
chips.set("0")
ugali.set("0")
githeri.set("0")
mokimo.set("0")
chapati.set("0")
fish.set("0")

Date_of_Order.set(time.strftime("%d/%m/%y"))

# Declaration of Fxn-------------------------------------

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Total_of_Food.set("")
    Total_of_Drinks.set("")
    ServiceCharge.set("")
    textReceipt.delete("1.0", END)


    cocktail.set("0")
    iced_tea.set("0")
    hot_chocolate.set("0")
    juice.set("0")
    milkshake.set("0")
    water.set("0")
    soda.set("0")
    coffee.set("0")

    fried_chicken.set("0")
    fried_beef.set("0")
    chips.set("0")
    ugali.set("0")
    githeri.set("0")
    mokimo.set("0")
    chapati.set("0")
    fish.set("0")

    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8 .set(0)
    variable9 .set(0)
    variable10 .set(0)
    variable11 .set(0)
    variable12 .set(0)
    variable13 .set(0)
    variable14 .set(0)
    variable15 .set(0)
    variable16 .set(0)


    textCocktail.configure(state=DISABLED)
    textIcedTea.configure(state=DISABLED)
    textHotChocolate.configure(state=DISABLED)
    textJuice.configure(state=DISABLED)
    textMilkShake.configure(state=DISABLED)
    textWater.configure(state=DISABLED)
    textSoda.configure(state=DISABLED)
    textCoffee.configure(state=DISABLED)
    textFriedChicken.configure(state=DISABLED)
    textFriedBeef.configure(state=DISABLED)
    textChips.configure(state=DISABLED)
    textUgali.configure(state=DISABLED)
    textGitheri.configure(state=DISABLED)
    textMokimo.configure(state=DISABLED)
    textChapati.configure(state=DISABLED)
    textFish.configure(state=DISABLED)

def TotalofUnit():
    Unit1 = float(cocktail.get())
    Unit2 = float(iced_tea.get())
    Unit3 = float(hot_chocolate.get())
    Unit4 = float(juice.get())
    Unit5 = float(milkshake.get())
    Unit6 = float(water.get())
    Unit7 = float(soda.get())
    Unit8 = float(coffee.get())

    Unit9 = float(fried_chicken.get())
    Unit10 = float(fried_beef.get())
    Unit11 = float(chips.get())
    Unit12 = float(ugali.get())
    Unit13 = float(githeri.get())
    Unit14 = float(mokimo.get())
    Unit15 = float(chapati.get())
    Unit16 = float(fish.get())

    Prices_Drinks = (Unit1 * 100) + (Unit2 * 50) + (Unit3 * 70) + (Unit4 * 50) + (Unit5 * 70) + (Unit6 * 30) + (Unit7 * 70) + (Unit8 * 70)

    Prices_Food = (Unit9 * 100) + (Unit10 * 80) + (Unit11 * 100) + (Unit12 * 50) + (Unit13 * 70) + (Unit14 * 100) + (Unit15 * 30) + (Unit16 * 100)



    DrinksPrices = "KES" + str('%.2f' % Prices_Drinks)
    FoodsPrices = "KES" + str('%.2f' % Prices_Food)
    Total_of_Food.set(FoodsPrices)
    Total_of_Drinks.set(DrinksPrices)
    SC = "KES" + str('%.2f' % 10)
    ServiceCharge.set(SC)

    Sub_Total_of_Unit = "KES" + str('%.2f'%(Prices_Drinks + Prices_Food + 10))
    SubTotal.set(Sub_Total_of_Unit)

    Tax = "KES" + str('%.2f'%((Prices_Drinks + Prices_Food + 10) * 0.10))
    PaidTax.set(Tax)

    TT = ((Prices_Drinks + Prices_Food + 10) * 0.10)
    TC = "KES" + str('%.2f'%(Prices_Drinks + Prices_Food + 10 + TT))
    TotalCost.set(TC)


def drinksCocktail():
    if variable1.get() == 1:
        textCocktail.configure(state=NORMAL)
        textCocktail.focus()
        textCocktail.delete('0', END)
        cocktail.set("")
    elif variable1.get() == 0:
        textCocktail.configure(state=DISABLED)
        cocktail.set("0")

def drinksIceTea():
    if variable2.get() == 1:
        textIcedTea.configure(state=NORMAL)
        textIcedTea.focus()
        textIcedTea.delete('0', END)
        iced_tea.set("")
    elif variable2.get() == 0:
        textIcedTea.configure(state=DISABLED)
        iced_tea.set("0")

def drinksHotChocolate():
    if variable3.get() == 1:
        textHotChocolate.configure(state=NORMAL)
        textHotChocolate.delete('0', END)
        textHotChocolate.focus()
    elif variable3.get() == 0:
        textHotChocolate.configure(state=DISABLED)
        hot_chocolate.set("0")

def drinksJuice():
    if variable4.get() == 1:
        textJuice.configure(state=NORMAL)
        textJuice.delete('0', END)
        textJuice.focus()
    elif variable4.get() == 0:
        textJuice.configure(state=DISABLED)
        juice.set("0")

def drinksMilkShake():
    if variable5.get() == 1:
        textMilkShake.configure(state=NORMAL)
        textMilkShake.delete('0', END)
        textMilkShake.focus()
    elif variable5.get() == 0:
        textMilkShake.configure(state=DISABLED)
        milkshake.set("0")

def drinksWater():
    if variable6.get() == 1:
        textWater.configure(state=NORMAL)
        textWater.delete('0', END)
        textWater.focus()
    elif variable6.get() == 0:
        textWater.configure(state=DISABLED)
        water.set("0")

def drinksSoda():
    if variable7.get() == 1:
        textSoda.configure(state=NORMAL)
        textSoda.delete('0', END)
        textSoda.focus()
    elif variable7.get() == 0:
        textSoda.configure(state=DISABLED)
        soda.set("0")

def drinksCoffee():
    if variable8.get() == 1:
        textCoffee.configure(state=NORMAL)
        textCoffee.delete('0', END)
        textCoffee.focus()
    elif variable8.get() == 0:
        textCoffee.configure(state=DISABLED)
        coffee.set("0")

def foodsFriedChicken():
    if variable9.get() == 1:
        textFriedChicken.configure(state=NORMAL)
        textFriedChicken.delete('0', END)
        textFriedChicken.focus()
    elif variable9.get() == 0:
        textFriedChicken.configure(state=DISABLED)
        fried_chicken.set("0")

def foodsFriedBeef():
    if variable10.get() == 1:
        textFriedBeef.configure(state=NORMAL)
        textFriedBeef.delete('0', END)
        textFriedBeef.focus()
    elif variable10.get() == 0:
        textFriedBeef.configure(state=DISABLED)
        fried_beef.set("0")

def foodsChips():
    if variable11.get() == 1:
        textChips.configure(state=NORMAL)
        textChips.delete('0', END)
        textChips.focus()
    elif variable11.get() == 0:
        textChips.configure(state=DISABLED)
        chips.set("0")

def foodsUgali():
    if variable12.get() == 1:
        textUgali.configure(state=NORMAL)
        textUgali.delete('0', END)
        textUgali.focus()
    elif variable12.get() == 0:
        textUgali.configure(state=DISABLED)
        ugali.set("0")

def foodsGitheri():
    if variable13 .get() == 1:
        textGitheri.configure(state=NORMAL)
        textGitheri.delete('0', END)
        textGitheri.focus()
    elif(variable13.get() == 0):
        textGitheri.configure(state=DISABLED)
        githeri.set("0")

def foodsMokimo():
    if variable14 .get() == 1:
        textMokimo.configure(state=NORMAL)
        textMokimo.delete('0', END)
        textMokimo.focus()
    elif variable14.get() == 0:
        textMokimo.configure(state=DISABLED)
        mokimo.set("0")

def foodsChapati():
    if variable15.get() == 1:
        textChapati.configure(state=NORMAL)
        textChapati.delete('0', END)
        textChapati.focus()
    elif variable15.get() == 0:
        textChapati.configure(state=DISABLED)
        chapati.set("0")

def foodsFish():
    if variable16 .get() == 1:
        textFish.configure(state=NORMAL)
        textFish.delete('0', END)
        textFish.focus()
    elif(variable16.get() == 0):
        textFish.configure(state=DISABLED)
        fish.set("0")

def Receipt():
    textReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)


    textReceipt.insert(END, 'Receipt No:\t\t\t'+Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
    textReceipt.insert(END, 'Unit\t\t\t\t'+"Total of Unit \n")
    textReceipt.insert(END, 'Cocktail:\t\t\t\t\t' + cocktail.get() + '\n')
    textReceipt.insert(END, 'Iced Tea:\t\t\t\t\t' + iced_tea.get()+'\n')
    textReceipt.insert(END, 'Hot Chocolate:\t\t\t\t\t' + hot_chocolate.get()+'\n')
    textReceipt.insert(END, 'Juice:\t\t\t\t\t' + juice.get() + '\n')
    textReceipt.insert(END, 'Milk Shake:\t\t\t\t\t' + milkshake.get()+'\n')
    textReceipt.insert(END, 'Water:\t\t\t\t\t' + water.get() + '\n')
    textReceipt.insert(END, 'Soda:\t\t\t\t\t' + soda.get() + '\n')
    textReceipt.insert(END, 'Coffee:\t\t\t\t\t' + coffee.get() + '\n')
    textReceipt.insert(END, 'Fried Chicken:\t\t\t\t\t' + fried_chicken.get()+'\n')
    textReceipt.insert(END, 'Fried Beef:\t\t\t\t\t' + fried_beef.get() + '\n')
    textReceipt.insert(END, 'Chips:\t\t\t\t\t' + chips.get() + '\n')
    textReceipt.insert(END, 'Ugali:\t\t\t\t\t' + ugali.get() + '\n')
    textReceipt.insert(END, 'Githeri:\t\t\t\t\t' + githeri.get() + '\n')
    textReceipt.insert(END, 'Mokimo:\t\t\t\t\t' + mokimo.get() + '\n')
    textReceipt.insert(END, 'Chapati:\t\t\t\t\t' + chapati.get() + '\n')
    textReceipt.insert(END, 'Fish:\t\t\t\t\t' + fish.get() + '\n')
    textReceipt.insert(END, 'Total of Starter:\t\t\t\t' + Total_of_Drinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    textReceipt.insert(END, 'Total of Main Course:\t\t\t\t' + Total_of_Food.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    textReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


# Starters----------------------------------------------------
lblStarterPart=Label(Drinks_Function, font=('arial',20,'bold','italic','underline'),text='Drinks for Starter',
               bg='sky blue',fg='black',justify=CENTER).grid(row=0)

Cocktail = Checkbutton(Drinks_Function, text='Cocktail', variable=variable1, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksCocktail).grid(row=1, sticky=W)
IcedTea = Checkbutton(Drinks_Function, text='Iced Tea', variable=variable2, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksIceTea).grid(row=2, sticky=W)
HotChocolate = Checkbutton(Drinks_Function, text='Hot Chocolate', variable=variable3, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksHotChocolate).grid(row=3, sticky=W)
Juice = Checkbutton(Drinks_Function, text='Juice', variable=variable4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksJuice).grid(row=4, sticky=W)
MilkShake = Checkbutton(Drinks_Function, text='Milk Shake', variable=variable5, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksMilkShake).grid(row=5, sticky=W)
Water = Checkbutton(Drinks_Function, text='Water', variable=variable6, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksWater).grid(row=6, sticky=W)
Soda = Checkbutton(Drinks_Function, text='Soda', variable=variable7, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksSoda).grid(row=7, sticky=W)
Coffee = Checkbutton(Drinks_Function, text='Coffee', variable=variable8, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksCoffee).grid(row=8, sticky=W)

# Drink Entry
textCocktail = Entry(Drinks_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=cocktail)
textCocktail.grid(row=1,column=1)

textIcedTea = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=iced_tea)
textIcedTea.grid(row=2,column=1)

textHotChocolate = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=hot_chocolate)
textHotChocolate.grid(row=3,column=1)

textJuice= Entry(Drinks_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=juice)
textJuice.grid(row=4,column=1)

textMilkShake = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=milkshake)
textMilkShake.grid(row=5,column=1)

textWater = Entry(Drinks_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=water)
textWater.grid(row=6,column=1)

textSoda = Entry(Drinks_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=soda)
textSoda.grid(row=7,column=1)

textCoffee = Entry(Drinks_Function, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=coffee)
textCoffee.grid(row=8,column=1)

# Main Course---------------------------------------------
lblMainCourse=Label(Food_Function, font=('arial',20,'bold','italic','underline'),text='Foods for Main Course',
               bg='sky blue',fg='black',justify=CENTER).grid(row=0)

FriedChicken = Checkbutton(Food_Function,text="Fried Chicken\t\t\t ",variable=variable9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsFriedChicken).grid(row=1,sticky=W)
FriedBeef = Checkbutton(Food_Function, text="Fried Beef ", variable=variable10, onvalue = 1, offvalue=0,
                       font=('arial',16,'bold'), bg='sky blue', command=foodsFriedBeef).grid(row=2, sticky=W)
Chips = Checkbutton(Food_Function, text="Chips ", variable=variable11, onvalue = 1, offvalue=0,
                         font=('arial',16,'bold'), bg='sky blue', command=foodsChips).grid(row=3, sticky=W)
Ugali = Checkbutton(Food_Function, text="Ugali ", variable=variable12, onvalue = 1, offvalue=0,
                            font=('arial',16,'bold'), bg='sky blue', command=foodsUgali).grid(row=4, sticky=W)
Githeri = Checkbutton(Food_Function,text="Githeri ",variable=variable13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsGitheri).grid(row=5,sticky=W)
Mokimo = Checkbutton(Food_Function, text="Mokimo ", variable=variable14, onvalue = 1, offvalue=0,
                           font=('arial',16,'bold'), bg='sky blue', command=foodsMokimo).grid(row=6, sticky=W)
Chapati = Checkbutton(Food_Function, text="Chapati ", variable=variable15, onvalue = 1, offvalue=0,
                            font=('arial',16,'bold'), bg='sky blue', command=foodsChapati).grid(row=7, sticky=W)
Fish = Checkbutton(Food_Function, text="Fish ", variable=variable16, onvalue = 1, offvalue=0,
                           font=('arial',16,'bold'), bg='sky blue', command=foodsFish).grid(row=8, sticky=W)

#Entry
textFriedChicken=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=fried_chicken)
textFriedChicken.grid(row=1,column=1)

textFriedBeef=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=fried_beef)
textFriedBeef.grid(row=2, column=1)

textChips=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=chips)
textChips.grid(row=3, column=1)

textUgali=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=ugali)
textUgali.grid(row=4, column=1)

textGitheri=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=githeri)
textGitheri.grid(row=5, column=1)

textMokimo=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=mokimo)
textMokimo.grid(row=6, column=1)

textChapati=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=chapati)
textChapati.grid(row=7, column=1)

textFish=Entry(Food_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=fish)
textFish.grid(row=8, column=1)

# ToTal Cost
lblTotalofDrinks=Label(Total_Function,font=('arial',14,'bold'),text='Total of Drinks\t',bg='sky blue',fg='black',justify=CENTER)
lblTotalofDrinks.grid(row=0,column=0,sticky=W)
textTotalofDrinks=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Drinks)
textTotalofDrinks.grid(row=0,column=1)

lblTotalofFood=Label(Total_Function,font=('arial',14,'bold'),text='Total of Foods  ',bg='sky blue',fg='black',justify=CENTER)
lblTotalofFood.grid(row=1,column=0,sticky=W)
textTotalofFood=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Food)
textTotalofFood.grid(row=1,column=1)

lblServiceCharge=Label(Total_Function,font=('arial',14,'bold'),text='Service Charge',bg='sky blue',fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)

# Payment information
lblPaidTax=Label(Total_Function,font=('arial',14,'bold'),text='\tPaid Tax',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
textPaidTax=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=PaidTax)
textPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Total_Function,font=('arial',14,'bold'),text='\tSub Total',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
textSubTotal=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'), insertwidth=2,justify=RIGHT,textvariable=SubTotal)
textSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Total_Function,font=('arial',14,'bold'),text='\tTotal',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
textTotalCost=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
textTotalCost.grid(row=2,column=3)

# RECEIPT
textReceipt=Text(Receipt_Function,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
textReceipt.grid(row=0,column=0)


# BUTTONS
buttonTotal=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Total',bg='black',command=TotalofUnit).grid(row=0,column=0)
buttonReceipt=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Receipt',bg='black',command=Receipt).grid(row=0,column=1)
buttonReset=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Reset',bg='black',command=Reset).grid(row=0,column=2)
buttonExit=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Exit',bg='black',command=iExit).grid(row=0,column=3)


# Calculator Display

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




# Calculator
txtDisplay = Entry(Calculator_Function, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

# Buttons
button7=Button(Calculator_Function, padx=16, pady=1, bd=7, fg='gold', font=('arial', 12, 'bold'), width=4, text='7',bg='black',command=lambda:btnClick(7)).grid(row=2,column=0)
button8=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='8',bg='black',command=lambda:btnClick(8)).grid(row=2,column=1)
button9=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='9',bg='black',command=lambda:btnClick(9)).grid(row=2,column=2)
buttonAdd=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='+',bg='black',command=lambda:btnClick('+')).grid(row=2,column=3)

button4=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='4',bg='black',command=lambda:btnClick(4)).grid(row=3,column=0)
button5=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='5',bg='black',command=lambda:btnClick(5)).grid(row=3,column=1)
button6=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='6',bg='black',command=lambda:btnClick(6)).grid(row=3,column=2)
buttonSub=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='-',bg='black',command=lambda:btnClick('-')).grid(row=3,column=3)

button1=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='1',bg='black',command=lambda:btnClick(1)).grid(row=4,column=0)
button2=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='2',bg='black',command=lambda:btnClick(2)).grid(row=4,column=1)
button3=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='3',bg='black',command=lambda:btnClick(3)).grid(row=4,column=2)
buttonMulti=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='*',bg='black',command=lambda:btnClick('*')).grid(row=4,column=3)

button0=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='0',bg='black',command=lambda:btnClick(0)).grid(row=5,column=0)
buttonClear=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='C',bg='black',command=btnClear).grid(row=5,column=1)
buttonEqual=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='=',bg='black',command=btnEquals).grid(row=5,column=2)
buttonDiv=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='/',bg='black',command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()

