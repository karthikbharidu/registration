def register():
    details={}
    print("---------REGISTER HERE-----------")
    username=input("ENTER YOUR NAME:").strip()
    password=input("ENTER YOUR PASSWORD:" )
    re_password=input("RE_TYPE YOUR PASSWORD:")
    if(password==re_password):
        print("REGISTRED SUCCESSFULLY")
    else:
        print("PASSWORDS DO NOT MATCH")
        password2=input("ENTER YOUR PASSWORD:")
        if(password2==password):
            print("REGISTERED SUCCESSFULL")
            pass
            
        else:
            print("PASSWORDS ARE NOT MATCH")
            password3=input("ENTER YOUR PASSWORD:")
            if(password3==password):
                print("REGISTERED SUCCESSFULL")
                pass
            else:
                print("TOO MANY ATTEMPTS!!! TRY AGAIN LATER")
                pass

    details[username]=password
    
    #this is Login page
    c=int(input("ENTER 1 TO LOGIN PAGE , ENTER 0 TO EXIT:"))
    if(c==1):
        print("-------LOGIN HERE-------")
        user=input("ENTER YOUR USERNAME:")     
        passw=input("ENTER YOUR PASSWORD:")
       # print(details.keys(),details.values())
        if (user in details.keys() and passw in details.values()):
            print("LOGIN SUCCESSFUL")
            print("HELLO",user)
        else: 
            print("INVALID CREDENTIALS")
            f=int(input("IF YOU WANT TO CHANGE YOUR PASSWORD!! ENTER 2 ,ENTER 0 TO EXIT"))
            if(f==2):
                  cha_user=input("ENTER YOUR USERNAME:")
                  if(cha_user in details.keys()):
                      print("------UPDATE HERE-------")
                      cha_pass=input("ENTER NEW PASSWORD:")
                      re_cha_pass=input("RE_ENTER NEW PASSWORD:")
                      if(cha_pass==re_cha_pass):
                          details[cha_user]=cha_pass
                          print("PASSWORD UPDATE SUCCESSFULLY!!")
                          m=input("ENTER YES TO LOGIN ,NO TO CONTINUE:")
                          if(m=="YES" or m=="yes"):
                              user_re=input("ENTER YOUR USER NAME:")
                              pass_re=input("ENTER YOUR PASSWORD:")
                              if(user_re in details.keys() and pass_re in details.values()):
                                  print("LOGIN SUCCESSFUL!!")
                              else:
                                  print("LOGIN FAILED")
                          elif(m=="NO" or m=="no"):
                              print("THANK YOU COMEBACK LATER")
                              
                      else:
                          print("PASSWORDS DO NOT MATCH")
                  else:
                      print("SORRY!! YOU ARE NOT REGISTERED WITH US")
                  
                  
        
    elif(c==0):
                  
        print("THANK YOU FOR REGISTERED WITH US")
            
    
            
                
        
    

register()

    
    
    

