import csv
import os
import pandas as pd

def clear_terminal():
    """
    Clear the terminal/console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("CODED BY PRASH \n")


class fileClass:
    def __init__(self,filename) -> None:
        self.filename = filename
    
    def display_all_items(self):
        with open(self.filename,'r') as f:
            fil = csv.reader(f)
            for i in fil:
                for j in i:
                    print(j , end="\t")
                print()
            input()

    def display_half(self):
        with open(self.filename,'r') as f:
            fil = csv.reader(f)
            for i in fil:
                for j in range(2):
                    print(i[j] , end="\t")
                print()

    def add_new_item(self,name,quantity, costprice , sellingprice):
        with open(self.filename,'r+', newline="") as f:
            fil = csv.writer(f)
            li = [len(list(csv.reader(f))),name, quantity , costprice, sellingprice]
            fil.writerow(li)
        print("Item Sucessfully Added")
        input()

    def delete(self,name):
        with open(self.filename) as f:
            fil = csv.reader(f)
            flag = False
            temp_list = list(fil)
            print(temp_list)
            for i in temp_list:
                if i[1] == name:
                    o = temp_list.index(i)
                    temp_list.remove(i)

            for j in range(o,len(temp_list)):
                temp_list[j][0] = int(temp_list[j][0])-1
                
        with open(self.filename, 'w', newline="") as f:
            c = csv.writer(f)
            for i in temp_list:
                c.writerow(i)
        print("Item sucessfully Deleted! ")
        input()

    def edit_Itemname(self,sn,name): 
        with open(self.filename,'r') as f:
            b = csv.reader(f)
            a = list(b)
        if sn < len(a):
            df = pd.read_csv(self.filename)
            df.loc[sn-1 , 'ITEM'] = name 
            df.to_csv(self.filename, index=False)
        else:
            print("SN is not matched, Try entering again")

    def edit_quantity(self,sn,qty): 
        with open(self.filename,'r') as f:
            b = csv.reader(f)
            a = list(b)
        if sn > len(a):    
            df = pd.read_csv(self.filename)
            df.loc[sn-1 , 'QTY'] = qty 
            df.to_csv(self.filename, index=False)
        else:
            print("SN is not matched, Try entering again")

    def edit_cp(self,sn,cp):   
        with open(self.filename,'r') as f:
            b = csv.reader(f)
            a = list(b)
        if sn > len(a):  
            df = pd.read_csv(self.filename)
            df.loc[sn-1 , 'CP'] = cp 
            df.to_csv(self.filename, index=False)
        else:
            print("SN is not matched, Try entering again")

    def edit_sp(self,sn,SP): 
        with open(self.filename,'r') as f:
            b = csv.reader(f)
            a = list(b)
        if sn > len(a):    
            df = pd.read_csv(self.filename)
            df.loc[sn-1 , 'SP'] = SP 
            df.to_csv(self.filename, index=False)
        else:
            print("SN is not matched, Try entering again")

    def search_by(self,arg,what):
        with open(self.filename) as f:
            fil = csv.reader(f)
            flag = False
            for i in fil:
                if i[int(arg)].lower() == what:
                    print(f'sn = {i[0]} \t item = {i[1]} \t quantity = {i[2]} \t cp = {i[3]} \t sp = {i[4]}')
                    flag = True
            if flag == False:
                print("Item not found or spelling is error.You can try manually checking the file")
            input()

    def sold(self,name,piece):
        with open(self.filename) as f:
            fil = csv.reader(f)
            flag = False
            for i in fil:
                if i[1] == name:
                    a = int(i[0])
                    q = int(i[2])
                    flag = True
        if flag:
            df = pd.read_csv(self.filename)
            df.loc[a-1 , 'QTY'] = q - piece 
            df.to_csv(self.filename, index=False)
            print("operation completed")
        else:
            print("There was a problem doing that operation , maybe your spelling is wrong")


def main():
    while True:
        clear_terminal()
        print('1. Stationary')
        print('2. Gift')
        print('3. Gifts and Toys')
        x = input('Choose which you want to alter? Enter number : ').strip()
        clear_terminal()
        match x:
            case '1':
                a = fileClass('stationary.csv')
            case '2':
                a = fileClass('gifts.csv')
            case '3':
                a = fileClass('toys_and_dolls.csv')
            case '4':
                a = fileClass('others.csv')
        print("1. Show all Items")
        print("2. Add a new Item")
        print("3. Search Item")
        print("4. Edit item info")
        print("5. sold ")
        print("6. Delete an item ")
        y = input('>>>>').strip()
        match y:
            case '1':
                a.display_all_items()
            case '2':
                a.add_new_item(input('name: '), int(input('quantity: ')),int(input('Cost Price: ')),int(input('Selling Price: ')) )
                clear_terminal()
            case '3':
                clear_terminal()
                print('1. By SN')
                print('2. By Item Name')
                print('3. By quantity')
                print('4. By cp')
                print('5. By sp')
                y = int(input('>>>>').strip())
                z = input('Value to search?: ').lower()
                a.search_by(y-1,z)
            case '4':
                clear_terminal()
                a.display_all_items()
                sn = int(input('Sn of the item which you want to edit: ').strip())
                print("1. Name")
                print("2. Quantity")
                print("3. CP")
                print("4. SP")
                y = input("What do you want to edit?: ")
                match y:
                    case '1':
                        a.edit_Itemname(sn=sn , name =input("New Name: "))
                    case '2':
                        a.edit_quantity(sn=sn , qty= input("New quantity: "))
                    case '3':
                        a.edit_cp(sn=sn , cp= input("New CP: "))
                    case '4':
                        a.edit_sp(sn=sn , SP= input("New SP: "))
                input()
                clear_terminal()
                print('Item sucessfully updated!')
            case '5':
                a.display_all_items()
                name = input('Name of the Item: ')
                a.sold(name, int(input('How many pieces are sold?: ').strip()))
                print()
                a.search_by(1,name)
            case '6':
                a.display_half()
                a.delete(input("item Name: ").lower().strip())




main()
