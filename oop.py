class magicalcontacts:
    def __init__(self,name,num,email):
        self.name=name
        self.num=num
        self.email=email

    def get_name(self):
        print(self.name) 
    
    def get_num(self):
        print(self.num) 
    
    def get_email(self):
        print(self.email) 
    
    def set_num(self,newnum):
        self.num=newnum
        print(newnum)

    def set_email(self,newemail):
        self.email=newemail
        print(newemail)
    
    def describe(self):
        print(f"name:{self.name} , num:{self.num} , email:{self.email}")

me=magicalcontacts("jannat","127542","jane.com")
me.set_num('1234')
me.describe()
lst=["gryffindor","hufflepuff","ravenclaw","slytherin"]
class witch(magicalcontacts):
    def __init__(witchh,wand_core,wand_wood,wand_length,house):
            witchh.wand_core=wand_core
            witchh.wand_wood=wand_wood
            witchh.wand_length=wand_length
            witchh.house=house

    def get_core(witchh):
            print(witchh.wand_core) 

    def get_wood(witchh):
            print(witchh.wand_wood)

    def get_length(witchh):
            print(witchh.wand_length)
    h=True
    def set_house(witchh,home):
            witch.house=home
            for home in lst:
                if home in lst:
                    #print(home)
                    h=True
                    continue
                else:
                    h=False
                    print("not found")
                    break
            if h==True:
                print(home)

    def des(witchh):
        print(f"core:{witchh.wand_core} , wood type:{witchh.wand_wood} , length:{witchh.wand_length} , wizard house:{witchh.house}")

home=input("enter house : ")
u=witch("phoenix feather","holly","10",home)
u.des() 


class book(magicalcontacts):
    def __init__(self,titl,phn,ml):
        self.title=titl
        self.nums=phn
        self.mail=ml

    def __str__(self):
         return f"{self.title} , {self.nums} , {self.mail}"
    
contacts=list()
users_input="" 
while users_input !="4":
        print("1 : enter contact")
        print("2 : view contacts")
        print("3 : find contact")
        print("4 : quit")
        users_input=input("select option: ")
        if users_input=="1":
                print("enter contacts info")
                titl=input("name: ")
                phn=input("num: ")
                ml=input("email: ")
                our_contact=book(titl,phn,ml)
                contacts.append(our_contact)
        elif users_input=="2":
                for contact in contacts:
                    print(contact)
        elif users_input=="3":
                srch=input("enter searched contact : ")
                for con in contacts:
                    if srch in contacts:
                        print(f"{srch}")
        elif users_input.lower=="4":
                break
        
our_c=book(titl,phn,ml)

