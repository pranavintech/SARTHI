from playsound import playsound
import mysql.connector
def datmaker():#database creation
    data = mysql.connector.connect( host="localhost",user="root",passwd="pranav")
    dat=data.cursor()
    dat.execute('SHOW DATABASES')
    if ('arogya',) not in dat:
        dat.execute('CREATE DATABASE arogya')
        print('')
    else:
        print('')
def tabmaker():#user input table
    table = mysql.connector.connect( host="localhost",user="root",passwd="pranav",database='arogya')
    curs = table.cursor()
    curs.execute('SHOW TABLES')
    if ('sarthi',) not in curs:
        curs.execute("CREATE TABLE sarthi(aadhaarno VARCHAR(14) not null primary key ,name VARCHAR(255), age INT(3),sex VARCHAR(8),weight INT(3), symptoms VARCHAR(300), AMC VARCHAR(250), zone VARCHAR(2))") 
        print('')
    else:
        print('')        
def clinmaker():#existing table
    db = mysql.connector.connect( host="localhost",user="root",passwd="pranav",database='arogya')
    cursor = db.cursor() 
    cursor.execute('SHOW TABLES')    
    if ('clinic',) not in cursor:
        cursor.execute("CREATE TABLE clinic(clinic VARCHAR(70), phoneno INT(11), address VARCHAR(100),zone varchar(2))")#this table could be uploaded on regular basis
        qu=('INSERT INTO clinic(clinic,phoneno,address,zone) VALUES(%s,%s,%s,%s)')
        val=('Mohalla clinic',111111111,'hno.20 tyagi mohalla','n')
        al=('Aam aadmi mohalla clinic',112211111,'gt road alipur,narela','n')
        lav=('Sri Gangaram hospital',111334111,'karol bagh','c')
        la=('BL Kapoor hospital',111111553,'patel nagar','c')
        vla=('Super Speciality',111111323,'saket','e')
        alv=('Apollo Indraprastha',111130311,'Indraprastha','e')
        valve=('Janakpuri super speciality hospital',114431111,'Janakpuri','w')
        evolve=('Deen Dayal Upadhyay',133311111,'Hari Nagar','w')
        volve=('Aakash Hospital',1111155531,'90/43, Malviya Nagar Rd','s')
        evl=('South Delhi Hospital',11999339,'A-5,Deol road','s')
        cursor.execute(qu,val)
        cursor.execute(qu,al)
        cursor.execute(qu,lav)
        cursor.execute(qu,la)
        cursor.execute(qu,vla)
        cursor.execute(qu,alv)
        cursor.execute(qu,valve)
        cursor.execute(qu,evolve)
        cursor.execute(qu,volve)
        cursor.execute(qu,evl)
        db.commit()
        print('')
    else :
        print('')
def vartalap():
    mydb = mysql.connector.connect( host="localhost",user="root",passwd="pranav",database='arogya')
    mycursor = mydb.cursor()#covid testing symptoms
    covid=['fever','dry cough','cough','cold','drycough','wet cough','wetcough','tiredness','head ache',
           'headache','body pain','bodypain','body pain','bodypain','neck pain','sore throat','soarthroat','diarrhoea'
           ,'vommiting','conjuctivities','tasteloss','loss of taste','smelllost','lost of smell','rashes','rashes on skin','skin rashes','discolouration of fingers',
           'finger discolouration',
           'toe discolouration','discolouration of toe','difficulty in breathing','difficult breathing','breathing difficulty','pain in chest', 'chest pain','pressure in chest',
           'increase chest pressure','jukam','jukaam','zukam','zukaam','balgam','thakan','thakaan','sir dard','badan dard','gale main kharash','gale main kharrash','dast','dast lagna',
           'gala dard', 'gale main dard','atisaar','ulti ana','ulti','ultiyan','ankhe ana','aankhe ana','aankhe anaa','netrashleshmakalashodh','svad ki haani','gandh ki hani',
           'chakatte','didore','laal chakatte','lal chakatte','chakatta','ungli ka rang udna','ungliyo ka rang udna','pairo ka rang udna', 'pair ka rang udna','saans lene main pareshani',
           'saans main dikkat','shwas rog','chhati main dard','chhati dard', 'chhati main dabaav','chhati main dabav','sirdard','khasi','seene main dard','seene main dabav']
    playsound('akshar.mp3')#request to answer in lower case
    print(' Kripya kar sare uttar lower case artharth chhote aksharo main hi de\n please write all answers in lower case only')
    playsound('swagat.mp3')#greeting
    print('Namastey  S.A.R.T.H.I app par apka swagat hai\nhello welcome to S.A.R.T.H.I app')
    x=int(input('Hindi ke liye 1 dabaye, press 2 for english:'))#language choice
    if x==1:#for Hindi
        playsound('hindresidence.mp3')#residential area for hospital recommendation
        sthan=input(' yadi aap uttar dilli ke niwasi hai to n dabaye\n yadi aap dakshin dilli ke niwasi hai to s dabaye\n yadi aap purab dilli ke niwasi hai to e dabaye\n yadi aap pashchim dilli ke niwasi hai to w dabaye\n yadi aap central dilli ke niwasi hai to c dabaye:')
        playsound('aadhaarhind.mp3')
        aadhaar=input(' kripya kar apna aadhaar number type kare:')
        playsound('naam.mp3')
        Naam=input('Naam type kare:')
        playsound('umra.mp3')
        Umra=int(input('umra type kare:'))
        playsound('ling.mp3')
        Ling=input('ling type kare:')
        playsound('vajan.mp3')
        Vajan=int(input('vajan type kare:'))
        playsound('lakshan.mp3')
        Lakshan=input('Lakshan type kare:')
        playsound('dava.mp3')
        Dava=input('Kya aap kisi anya dava ka sewan karte hai yadi haan to type kare:')#other medicine consumption asked to prevent drug reaction
        sql = "INSERT INTO sarthi (aadhaarno,name,age,sex,weight,symptoms,AMC,zone) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
        val = (aadhaar,Naam,Umra,Ling,Vajan,Lakshan,Dava,sthan)
        mycursor.execute(sql, val)
        mydb.commit()
        print('data added')
        for i in Lakshan.split(','):
            if i in covid:#covid symptoms
                print('Hame ye batate hue khed ho raha hai ki aapke kuch lakshan Covid-19 ke lakshano \nse milte hai kripya kar swayam ko quarantine karli jiye aur neeche bataye gaye\nchikitsalayo ki suchi main se kisi ek main jakar jaanch karaye.\nJaate samay mask avashya pehne aaur samajic doori banakar rahe')
                playsound('covidhindi.mp3')  
                if sthan=='n':#hospital zone recommendation
                        ql = "SELECT * FROM clinic WHERE zone = 'n' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                elif sthan=='s':
                        ql = "SELECT * FROM clinic WHERE zone = 's' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                elif sthan=='e':
                        ql = "SELECT * FROM clinic WHERE zone = 'e' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                elif sthan=='w':
                       ql = "SELECT * FROM clinic WHERE zone = 'w' "
                       mycursor.execute(ql)
                       an = mycursor.fetchall()
                       for co in an:
                          print(co)
                elif sthan=='c':
                        ql = "SELECT * FROM clinic WHERE zone = 'c' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                break         
            else :
              playsound('hindclinic.mp3')
              print('Aapke shatra ke kuch chikitsalyo ki suchi ye rahi')
              if sthan=='n':#non covid symptoms
                        ql = "SELECT * FROM clinic WHERE zone = 'n' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
              elif sthan=='s':
                        ql = "SELECT * FROM clinic WHERE zone = 's' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
              elif sthan=='e':
                        ql = "SELECT * FROM clinic WHERE zone = 'e' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
              elif sthan=='w':
                        playsound('hindclinic.mp3')
                        ql = "SELECT * FROM clinic WHERE zone = 'w' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
              elif sthan=='c':
                        ql = "SELECT * FROM clinic WHERE zone = 'c' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)         
    elif x==2:#english input
        playsound('engresidence.mp3')   
        Sthan=input(' if you are a resident of north Delhi then press n\n if you are a resident of east Delhi then press e\n if you are resident of west Delhi then press w\n if you are a resident of south Delhi then press s\n if you are a resident of central Delhi then press c.:')
        playsound('aadhaareng.mp3')
        Aadhaar=input('please type your aadhaar number:')
        playsound('name.mp3')
        Name=input('Please type your name:')
        playsound('age.mp3')
        Age=int(input('Please enter your age:'))
        playsound('sex.mp3')
        Sex=input('please type your sex:')
        playsound('weight.mp3')
        Weight=int(input('please type your weight:'))
        playsound('symptoms.mp3')
        Symptoms=input('please type your symptoms:')
        playsound('amc.mp3')
        Amc=input('Do you consume some other medicine if yes then please enter:')
        sql = "INSERT INTO sarthi (aadhaarno,name,age,sex,weight,symptoms,AMC,zone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (Aadhaar,Name,Age,Sex,Weight,Symptoms,Amc,Sthan)
        mycursor.execute(sql, val)
        mydb.commit()
        print('data added')
        for i in Symptoms.split(','):
            if i in covid:
                playsound('covideng.mp3')
                print('we are sorry to inform you that some of your symptoms match with Covid-19,\nplease quarantine yourselef and visit one of the clinic listed below.\n Please wear a mask while your visit and maintain social distancing') 
                if Sthan=='n':
                        ql = "SELECT * FROM clinic WHERE zone = 'n' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                elif Sthan=='s':
                        ql = "SELECT * FROM clinic WHERE zone = 's' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                elif Sthan=='e':
                        ql = "SELECT * FROM clinic WHERE zone = 'e' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                elif Sthan=='w':
                        ql = "SELECT * FROM clinic WHERE zone = 'w' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                elif Sthan=='c':
                        ql = "SELECT * FROM clinic WHERE zone = 'c' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                break         
                          
            else:
                  playsound('clinic.mp3')
                  print('This is the list of some clinics in your are')
                  if Sthan=='n':
                        ql = "SELECT * FROM clinic WHERE zone = 'n' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                  elif Sthan=='s':
                        ql = "SELECT * FROM clinic WHERE zone = 's' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                  elif Sthan=='e':
                        ql = "SELECT * FROM clinic WHERE zone = 'e' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                  elif Sthan=='w':
                        playsound('clinic.mp3')
                        ql = "SELECT * FROM clinic WHERE zone = 'w' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)
                  elif Sthan=='c':
                        ql = "SELECT * FROM clinic WHERE zone = 'c' "
                        mycursor.execute(ql)
                        an = mycursor.fetchall()
                        for co in an:
                          print(co)         
    else:
        playsound('error.mp3') and print('ERROR !!incorrect choice entered \n ',25*('* '))
def pattern_e(n=4):#Graphic display
      for i in range(1,n+1):
            print()
            for j in range(1,n+1-i):
                  print(" ",end="\t")
            for k in range(1,i+1):
                  print("*",end="\t")
            for l in range (1,i):
                  print("*",end="\t")

    
        
def rog():#code initaion
    print('RECEPTIONIST MODE')
    pattern_e()
    print('\nS.A.R.T.H.I(Systematic Application Regulating \nTotal Health Information) \ndeveloped by Pranav Arora\nclass XII-H \nHans Raj Model School\n',25*('* '))
    vartalap()
    print(' Thank you \n Aapka dhanyavaad \n',25*('* '))
    playsound('oneonly.mp3')
    playsound('anya.mp3')
    ch=input('Any more patient(y/n)\nkya koi anya patient hai=')
    while ch=='y':
        pattern_e()
        print(('\nS.A.R.T.H.I(Systematic Application Regulating \nTotal Health Information) \n developed by Pranav Arora \n class XII-H \n Hans Raj Model School') )
        vartalap()
        print(' Thank you \n Aapka dhanyavaad \n',25*('* '))
        playsound('oneonly.mp3')
        playsound('anya.mp3')
        ch=input('Any more patient(y/n)\nkya koi anya patient hai=')
    if ch=='n':
        print(' Thank you \n Aapka dhanyavaad \n' ,25*('* '))
        playsound('oneonly.mp3')        
def deletedata():
    deldb = mysql.connector.connect(host = "localhost", user = "root", password = "pranav", database = "arogya")
    delcursor = deldb.cursor()
    a= input("Enter aadhaar no")
    delsql = "Delete from sarthi where aadhaarno = %s"
    delcursor.execute(delsql,(a,))
    deldb.commit()
    print( "record deleted")
def updatedata():
    updb = mysql.connector.connect(host = "localhost", user = "root", password = "pranav", database = "arogya")
    upcursor = updb.cursor()
    adha = input("Enter aadhaar no=")
    nme= input("Enter updated name=")
    upage= int(input("Enter updated age="))
    upling= input("Enter updated sex=")
    upvajan= int(input("Enter updated weight="))
    uplakshan = input("Enter updated symptoms=")
    upamc=input('enter any other updated medications which are taken=')
    upsthan = input("Enter updated zone=")
    upsql = "Update sarthi set  name = %s, age = %s,sex = %s, weight = %s,symptoms = %s, AMC = %s,zone=%s where aadhaarno = %s"
    upval = (nme,upage,upling,upvajan,uplakshan,upamc,upsthan,adha) 
    upcursor.execute(upsql,upval)
    updb.commit()
    print("record updated")        
def displaydata():
    disdb = mysql.connector.connect(host = "localhost", user = "root",  password = "pranav", database = "arogya")
    discursor = disdb.cursor()
    discursor.execute("SELECT * FROM sarthi")
    disdat= discursor.fetchall()
    for nmn in disdat:
        print(nmn)

def search_record():
    seadb = mysql.connector.connect(host = "localhost", user = "root",  password = "pranav", database = "arogya")
    seacursor = seadb.cursor()
    an = input("Enter aadhaar number")
    seasql = "SELECT * FROM sarthi where aadhaarno = %s"
    seacursor.execute(seasql,(an,))
    searow = seacursor.fetchone()
    print(searow)
def minmaj():
      mindb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'pranav', database = 'arogya')
      mincursor = mindb.cursor()
      minchoice=int(input('if you want to see data of minors then press 1 \nif you want to see data of adults then press 2='))
      if minchoice==1:
          mincursor.execute('SELECT * FROM sarthi WHERE age<18')
          mindat = mincursor.fetchall()
          for minx in mindat:
              print(minx)
      elif minchoice==2:
          mincursor.execute('SELECT * FROM sarthi WHERE age>=18')
          majdat = mincursor.fetchall()
          for majx in majdat :
              print(majx)

def menu():
      while True :
            print('SUPERVISING MODE')
            print('========== MENU ===============================================')
            print('press 1 to update a record')
            print('press 2 to delete a record')
            print('press 3 to display all record')
            print('press 4 to search patients of a particular aadhaar no')
            print('press 5 To search for data of major/minor patients')
            print('press 6 to Exit')
            print('===============================================================')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                updatedata()
            elif choice == 2:
                deletedata()
            elif choice == 3:
                displaydata()
            elif choice == 4:
                search_record()
            elif choice == 5:
                minmaj()
            elif choice == 6 : 
                  print('Exiting...')
                  break
            else: print('Invalid Input !')
              
    
def choose_mode():
        mode=int(input('press 1 to select RECEPTIONIST mode \npress 2 to select SUPERVISING mode='))
        if mode==1:
            rog()
        elif mode==2:
            menu()
        else:
            print('error.... try again next time')

datmaker()              
tabmaker()
clinmaker()
choose_mode()              
