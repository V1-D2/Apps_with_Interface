#Libraries
from tkinter import *
import sys
from tkinter import messagebox


#Functions
def returnToMenu():
    root.destroy()
    rootForProducts.destroy()
def main_screen():
    global frame, root
    root.title("Product Market")
    root['bg'] = "#fafafa"
    root.geometry('300x250')
    root.resizable(width=True, height=True)
    frame.place(relwidth=1, relheight=1)
    startFrameForProducts.place(relwidth=1, relheight=1)
    Start = Label(startFrameForProducts, text="Here will be products", bg="green", font=60)
    Start2 = Label(startFrameForProducts, text="Enter to admin our user accaunt", bg="orange", font=60)
    Start.pack()
    Start2.pack()
    title = Label(frame, text="Choose who are you", bg="orange", font=50, width=100)
    title.pack()
    adminBtn = Button(frame, text="Admin", bg="red", width=20, font=40, command=admin_validating)
    adminBtn.place(x = 55, y = 90)
    userBtn = Button(frame, text="User", bg="red", width=20, font=40, command = user)
    userBtn.place(x = 55, y=123)
    exitBtn = Button(frame, text="Exit", bg="violet", width=20, font=40, command=close_program)
    exitBtn.place(x = 55, y = 200)
#For user
def user():
    global userFrame, rootForProducts
    frameForProducts.place(relwidth = 1, relheight = 1)
    allProducts = Label(rootForProducts, text = "All current purshues")
    allProducts.pack()
    for product in listOfPurchases:
        newPurchue = Label(rootForProducts ,text = str(product) + ": " + str(listOfPurchases[product]))
        newPurchue.pack()
    userFrame.place(relwidth =1, relheight = 1)
    title = Label(userFrame, text="Choose what you want to do", bg="orange", font=50, width=100)
    title.pack()
    frameForLeftBtn = Frame(userFrame, bg="cyan")
    frameForRightBtn = Frame(userFrame, bg="cyan")

    btnForSummaryCost = Button(userFrame, text="Show the summary cost", bg="red", width=20, font=40,
                                   command=summaryCost)
    btnForProductBiggestAmount = Button(frameForLeftBtn, text="Product biggest amount", bg="red", width=20, font=40,
                                     command=productWithTheBiggestAmount)
    btnForSmallestPrice = Button(frameForLeftBtn, text="The smallest price", bg="red", width=20, font=40,
                                    command=theSmallestPriceOfProduct)
    btnForAddingProduct = Button(frameForRightBtn, text="Add new product", bg="red", width=20, font=40,
                                 command=addingNewProductOrAmount)
    btnForDeletingProduct = Button(frameForRightBtn, text="Delete a product", bg="red", width=20, font=40,
                                   command=deletingAProduct)
    btnExit = Button(userFrame, text="Exit", bg="violet", width=20, font=40, command=close_program)
    btnToMainMenu = Button(userFrame, text="Return to menu", bg="violet", width=20, font=40, command=returnToMenu)
    btnForSummaryCost.pack()
    btnExit.pack(side="bottom")
    btnToMainMenu.pack(side="bottom")
    frameForLeftBtn.place(relwidth=0.4, relheight=0.3, x=0, y=80)
    frameForRightBtn.place(relwidth=0.5, relheight=0.3, x=160, y=80)
    btnForProductBiggestAmount.pack()
    btnForSmallestPrice.pack()
    btnForAddingProduct.pack()
    btnForDeletingProduct.pack()

def addingNewProductOrAmount():
    frameForAdding.place(relwidth = 1, relheight = 1)
    arrayOfFuturePurchases = []
    for product in listOfProducts.keys():
        arrayOfFuturePurchases.append((str(product)+": "+str(listOfProducts[product]["amount"])))
    print(arrayOfFuturePurchases)
    chooseTheProduct = Label(frameForAdding, text="Choose the product", bg="orange", font=50, width=100)
    chooseTheProduct.pack()
    btnForProduct = OptionMenu(frameForAdding, variable, *arrayOfFuturePurchases)
    btnForProduct.pack()
    chooseTheAmount = Label(frameForAdding, text="Choose how many will you take", bg="orange", font=50, width=100)
    chooseTheAmount.pack()
    newAmountOfProduct.pack()
    btnAdd = Button(frameForAdding, text="Add", bg="red", width=20, font=40, command = adding)
    btnAdd.pack()
def adding():
    global variable, root
    productToAdd = (variable.get()).split(":")[0]
    amountToAdd = int(newAmountOfProduct.get())
    if(productToAdd in listOfPurchases.keys()):
        listOfPurchases[productToAdd] += amountToAdd
        listOfProducts[productToAdd]["amount"] -= amountToAdd
    else:
        listOfPurchases[productToAdd] = amountToAdd
        listOfProducts[productToAdd]["amount"] = listOfProducts[productToAdd]["amount"] - int(amountToAdd)
    returnToMenu()

def deletingAProduct():
    frameForAdding.place(relwidth=1, relheight=1)
    arrayOfPurchases = []
    for product in listOfPurchases.keys():
        arrayOfPurchases.append((str(product) + ": " + str(listOfPurchases[product])))
    chooseTheProduct = Label(frameForAdding, text="Choose the product", bg="orange", font=50, width=100)
    chooseTheProduct.pack()
    btnForNewProduct = OptionMenu(frameForAdding, variableForDeleting, *arrayOfPurchases)
    btnForNewProduct.pack()
    chooseTheAmount = Label(frameForAdding, text="Choose how many will you delete", bg="orange", font=50, width=100)
    chooseTheAmount.pack()
    newAmountOfProductForDeleting.pack()
    btnAdd = Button(frameForAdding, text="Add", bg="red", width=20, font=40, command=deleting)
    btnAdd.pack()
def deleting():
    global variableForDeleting, root
    productToDelete = (variableForDeleting.get()).split(":")[0]
    amountToDelete =  int(newAmountOfProductForDeleting.get())
    listOfPurchases[productToDelete] -= amountToDelete
    listOfProducts[productToDelete]["amount"] += amountToDelete
    if(listOfPurchases[productToDelete] == 0):
        del(listOfPurchases[productToDelete])
    returnToMenu()


def summaryCost():
    global listOfProducts, listOfPurchases
    cost = 0
    for product in listOfPurchases.keys():
        cost += listOfPurchases[product]*listOfProducts[product]["price"]
    info_str = f'Your summary cost is: {cost}'
    messagebox.showinfo(title="Summary cost", message=info_str)
def productWithTheBiggestAmount():
    global listOfPurchases
    theBiggestAmount = 0
    for product in listOfPurchases:
        if(theBiggestAmount < listOfPurchases[product]):
            theBiggestAmount = listOfPurchases[product]
    info = "Products with the biggest amount:"+'\n'
    for product in listOfPurchases:
        if(theBiggestAmount == listOfPurchases[product]):
            info = info+str(product)+"|"
    messagebox.showinfo(title="Products with the biggest amount", message=info)
def  theSmallestPriceOfProduct():
    global listOfPurchases, listOfProducts
    theSmallestPrice = 100000000
    for product in listOfPurchases.keys():
        priceOfProduct = listOfPurchases[product]*listOfProducts[product]["price"]
        if(theSmallestPrice > priceOfProduct):
            theSmallestPrice = priceOfProduct
    info = "Products with the smallest price:"+'\n'
    for product in listOfPurchases.keys():
        priceOfProduct = listOfPurchases[product] * listOfProducts[product]["price"]
        if(priceOfProduct == theSmallestPrice):
            info = info + str(product) + "|"
    messagebox.showinfo(title="The smallest price of product", message=info)

#For Admin
def admin():
    global adminFrame
    frameForProducts.place(relwidth=1, relheight=1)
    allProducts = Label(rootForProducts, text="All current products")
    allProducts.pack()
    for product in listOfProducts:
        newPurchue = Label(rootForProducts, text=str(product) + ": Amount is " + str(listOfProducts[product]["amount"]) + ", Price is" + str(listOfProducts[product]["price"]))
        newPurchue.pack()
    adminFrame.place(relwidth = 1, relheight = 1)
    title = Label(adminFrame, text="Choose what you want to do with products", bg="orange", font=50, width=100)
    title.pack()
    frameForLeftBtn = Frame(adminFrame, bg="cyan")
    frameForRightBtn = Frame(adminFrame, bg="cyan")

    btnForShowingProducts = Button(adminFrame, text="Show all of the products", bg="red", width=20, font=40, command=changeTheList)
    btnForChangingTheAmount = Button(frameForLeftBtn, text="Change amount", bg="red", width=20, font=40, command=changeTheList)
    btnForChangingThePrice = Button(frameForLeftBtn, text="Change price", bg="red", width=20, font=40, command=changeTheList)
    btnForAddingProduct = Button(frameForRightBtn, text="Add new product", bg="red", width=20, font=40, command=changeTheList)
    btnForDeletingProduct = Button(frameForRightBtn, text="Delete a product", bg="red", width=20, font=40, command=changeTheList)
    btnExit = Button(adminFrame, text="Exit", bg="violet", width=20, font=40, command=close_program)
    btnToMainMenu = Button(adminFrame, text="Return to menu", bg="violet", width=20, font=40, command=returnToMenu)
    btnForShowingProducts.pack()
    btnExit.pack(side="bottom")
    btnToMainMenu.pack(side = "bottom")
    frameForLeftBtn.place(relwidth=0.4, relheight=0.3, x = 0, y = 80)
    frameForRightBtn.place(relwidth=0.5, relheight=0.3, x = 160, y = 80)
    btnForChangingThePrice.pack()
    btnForChangingTheAmount.pack()
    btnForAddingProduct.pack()
    btnForDeletingProduct.pack()

def admin_validating():
    global closingFrame, passwordField, loginField, frame
    closingFrame.place(relwidth=1, relheight=1)
    title = Label(closingFrame, text="Enter to accaunt", bg="orange", font=50, width=100)
    loginTitle = Label(closingFrame, text = "Login", font = 30, bg = "green")
    passwordTitle = Label(closingFrame, text = "Password", font = 30, bg = "green")
    title.pack()
    loginTitle.pack()
    loginField.pack()
    passwordTitle.pack()
    passwordField.pack()
    chekingBtn = Button(closingFrame, text="Log in", bg="red", width=20, font=40, command = cheking)
    chekingBtn.pack()
    btnExit = Button(closingFrame, text="Exit", bg="violet", width=20, font=40, command=close_program)
    btnExit.pack(side = BOTTOM)


def cheking():
    login = loginField.get()
    password = passwordField.get()
    if ((login == "admin" or login == "Admin") and password == "log"):
        admin()
    else:
        info_str = f'Простите но такого аккаунта не существует'
        info_str = info_str + '\n' + f'Ваш логин:{login}, ваш пароль: {password}'
        messagebox.showinfo(title="Error", message=info_str)

def changeTheList():
    adminFrameForChangingAmount.place(relwidth = 1, relheight = 1)
    enterName = Label(adminFrameForChangingAmount ,text = "Enter the name of product", bg = "green")
    enterAmount = Label(adminFrameForChangingAmount  ,text = "Enter the amount of product", bg = "green")
    enterPrice = Label(adminFrameForChangingAmount, text = "Enter a price", bg ="green")
    enterName.pack()
    adminFieldForProductName.pack()
    enterAmount.pack()
    adminFieldForProductAmount.pack()
    enterPrice.pack()
    adminFieldForPrice.pack()
    btnGoNext = Button(adminFrameForChangingAmount ,text = "change", command = change)
    btnGoNext.pack()
def change():
    global adminFieldForProductName
    Name = adminFieldForProductName.get()
    Amount = int(adminFieldForProductAmount.get())
    Price = int(adminFieldForPrice.get())
    if(Name not in listOfProducts):
        listOfProducts[Name] = {"amount":Amount, "price":Price}
    elif(Amount == 0):
        del(listOfProducts[Name])
    else:
        listOfProducts[Name] = {"amount":Amount, "price":Price}
    returnToMenu()



#For exit
def close_program():
    sys.exit()


#Values
listOfProducts = {"Картошка" :{"amount": 25, "price":75},
                  "Гречка":{"amount": 25, "price":75},
                  "Рис": {"amount": 25, "price":75},
                  "Bread":{"amount": 25, "price":75}}
listOfPurchases = {}


#Main
while(True):
    root = Tk()
    rootForProducts = Tk()
    #Root for showing products
    rootForProducts['bg'] = "#fafafa"
    rootForProducts.title("List of purshues")
    rootForProducts.geometry('300x250')
    rootForProducts.resizable(width=True, height=True)
    #
    #Start screen for products
    startFrameForProducts = Frame(rootForProducts, bg="green")
    #
    #User screen for products
    frameForProducts = Frame(rootForProducts, bg="green")
    #Screen for main screen
    frame = Frame(root, bg="green")
    closingFrame = Frame(root, bg="green")
    adminFrame = Frame(root, bg="cyan")
    userFrame = Frame(root, bg="cyan")
    frameForDeleting = Frame(root, bg = "green")

    adminFrameForChangingAmount = Frame(root, bg="green")
    loginField = Entry(closingFrame, bg="white")
    passwordField = Entry(closingFrame, bg="white", show="*")
    adminFieldForProductName = Entry(adminFrameForChangingAmount, bg = "white")
    adminFieldForProductAmount = Entry(adminFrameForChangingAmount, bg = "white")
    adminFieldForPrice = Entry(adminFrameForChangingAmount, bg = "white")


    frameForAdding = Frame(root, bg = "green")
    variable = StringVar(root)
    variableForDeleting = StringVar(root)
    newAmountOfProduct = Entry(frameForAdding, bg = "white")
    newAmountOfProductForDeleting = Entry(frameForAdding, bg ="white")
    main_screen()
    root.mainloop()

