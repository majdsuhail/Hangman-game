from random import randint,choices

def introduction():
 
    print("Guess the word (Game), you have 4 categories\nto choose from which are\n(fruits,animals,sports,countries) \n First you have to choose one category,\nyou can choose it by typing the category name or\ntyping the number of the category(from 1-4)\n")

introduction()

repeat=[]
while len(repeat)==0:

 fruits=['apple', 'avocado', 'banana', 'blackberry', 'blueberry', 'cherry', 'coconut', 'cucumber', 'date', 'dragonfruit', 'eggplant', 'fig', 'grape', 'guava', 'kiwi', 'lemon', 'lime', 'mandarine', 'mango', 'nut', 'olive', 'orange', 'papaya', 'peach', 'pear', 'pineapple', 'raisin', 'raspberry', 'strawberry', 'tomato', 'watermelon']
 
 animals=['alligator', 'ant', 'ape', 'armadillo', 'baboon', 'bat', 'bear', 'beaver', 'beebuffalo', 'butterfly', 'camel', 'cat', 'caterpillar', 'cheetah', 'chicken', 'chimpanzee', 'cobra', 'cockroach', 'crab', 'crocodile', 'crow', 'deer', 'dinosaur', 'dog', 'dogfish', 'dolphin', 'donkey', 'duck', 'eagle', 'eel', 'elephant', 'falcon', 'fish', 'flamingo', 'fly', 'fox', 'frog', 'gazelle', 'panda', 'giraffe', 'goat', 'goose', 'goldfish', 'gorilla', 'grasshopper', 'pig', 'hamster', 'hawk', 'horse', 'human', 'jaguar', 'jellyfish', 'kangaroo', 'koala', 'leopard', 'lion', 'lobster', 'locust', 'monkey', 'moose', 'mouse', 'mosquito', 'octopus', 'owl', 'parrot', 'penguin', 'pigeon', 'rabbit', 'raccoon', 'rat', 'rhino', 'salmon', 'sardine', 'scorpion', 'seahorse', 'seal', 'shark', 'sheep', 'snail', 'snake', 'spider', 'squid', 'squirrel', 'tiger', 'turkey', 'turtle', 'buffalo', 'whale', 'wolf', 'wolverine', 'woodpecker', 'worm', 'zebra']

 sports= ["football","baseball","basketball","tennis","soccer","swimming","karate","kungfu","cricket","bingbong","cycling","bowling","golf","running","boxing","darts"]
 
 countries=['Emirates', 'Afghanistan', 'Albania', 'Armenia', 'Antarctica', 'Argentina', 'Australia', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Brazil', 'Canada', 'Switzerland', 'Chile', 'Cameroon', 'China', 'Colombia', 'Cuba', 'Cyprus', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Spain', 'Ethiopia', 'Finland', 'France', 'United Kingdom', 'Georgia', 'Ghana', 'Greenland', 'Guinea', 'Greece', 'Hong Kong', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'India', 'Iraq', 'Iran', 'Iceland', 'Italy', 'Jersey', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Cambodia', 'Comoros', 'Korea', 'Kuwait', 'Lebanon', 'Srilanka', 'Liberia', 'Luxembourg', 'Libya', 'Morocco', 'Monaco', 'Madagascar', 'Mali', 'Myanmar', 'Mongolia', 'Malta', 'Mexico', 'Malaysia', 'Mozambique', 'Niger', 'Nigeria', 'Netherlands', 'Norway', 'Nepal', 'New Zealand', 'Oman', 'Philippines', 'Pakistan', 'Poland', 'Palestine', 'Portugal', 'Paraguay', 'Qatar', 'Romania', 'Serbia', 'Russia', 'Saudi Arabia', 'Sudan', 'Sweden', 'Singapore', 'Slovakia', 'Senegal', 'Somalia', 'Syria', 'Chad', 'Thailand', 'Tunisia', 'Turkey', 'Taiwan', 'Tanzania', 'Ukraine', 'Uganda', 'United States', 'Uruguay', 'Venezuela', 'Vietnam', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']         

 n2=2
 
 ver=[] 
 
 ctnmlist=["None"]
 
 c=[]
 
 c3=[]

 def play():
   
   user3=str(input("tab the return button to play again or tab any other button to finish program\n"))
   
   global ctnmlist
   del ctnmlist[:]
   
   global c
   del c[:]
   
   if len(user3)!=0:
    
    repeat.append(1)      
  
 user0=input("Enter the category name or number: ")
 
 user=user0.lower() 
 ctnm=ctnmlist  
 
 ctnm.append("fruits")  if user=="1" or user== "fruits" else None
 
 ctnm.append("animals") if user=="2"or user== "animals" else None
 
 ctnm.append("sports") if user=="3" or  user=="sports" else None
 
 ctnm.append("countries") if user=="4" or user=="countries" else None
 
 ctnm=ctnmlist[-1]  
   
 if ctnm=="None":
       print("category name or number was not found...\n")
       
 else:
   a=len(eval(ctnm))
   w=eval(ctnm)[randint(0,a-1)].lower()
   
   print("you choosed the {} category\n".format(ctnm))     
       
   print("The word has",len(w),"letters\nyou have 3 tries")
   
   def game():
    
    user1=input("\nEnter your guess: ")
    user2=user1.lower()
    
    if user2==w:
     
     print("\n***Congratulations, YOU WON***.....'",w.upper(),"'is the right word\n")
     
     global ver
     del ver[:]
     
     global n2
     n2=0
    
     play()
    
    elif user2=="hint":
        
      
      if len(c)!=2:
       
        
        
        c.append(1) 
        
        
        c4=[]
        
        def choice():
        
          c2=choices(w,k=1)
          c2="".join(c2)
          
          c4.append(c2)
          
          c2=c4[-1]
          
          if c2 in c3:
            choice()
          else:
            c3.append(c2)
        
        choice()
        
        c2=c4[-1]
        
        
        
        
    
         
        for i in w:
            
           if i == c2 :
             print(c2,end="")  
           elif i in c3:
              print(i,end="")
           else:
              print("-",end="")
                               
      else:
          
          print("you only can use 2 hint")
          
      game()
      
    else:
     
     ver.append(1)
     
     while n2!=0:
      if n2==1:
       
       print("\nwrong guess\nyou have",n2,"time left")
      
      else:
       
       print("\nwrong guess\nyou have",n2,"times left")
           
      n2=n2-1
     
      game()
          
   game()
   
   if len(ver)>=1:
   
      print("\nYou Lost, the correct word is '"+w+"'\n")
      
      play()
  
  
    

  
      
      
	    
