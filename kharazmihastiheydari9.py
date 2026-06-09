#تحلیل نمرات دانش اموز
import os
filename="grades.txt"
if os.path.exists(filename):
    with open(filename,"r")as f:
        data=eval(f.read())
    math_li=data["math"]
    english_li=data["english"]
    physics_li=data["physics"]
    chemistry_li=data["chemistry"]
    art_li=data["art"]
else:
    math_li=[]
    english_li=[]
    physics_li=[]
    chemistry_li=[]
    art_li=[]
def save_data():
    data={"math":math_li,"english":english_li,"physics":physics_li,"chemistry":chemistry_li,"art":art_li}
    with open(filename,"w")as f:
        f.write(str(data))
while True:

    print("Hello👋")
    print("1)Click to enter the scores📖🔖")
    print("2)Exit👋")
    x=int(input("Choose"))
    match x:
        case 1:
            print(("1)select subject💫"))
            c=int(input("choose"))
            match c:
                case 1:
                    print("1)add score")
                    print("2)delete score")
                    print("3)average")
                    print("4)best and worst")  
                    b=int(input("choose"))
                    match b:
                        case 1:
                            print("Select subject to add the score")
                            print("1)Math🔢")
                            print("2)English🦋")
                            print("3)Physics🌍")
                            print("4)Chemistry👩‍🔬")
                            print("5)Art✏️")
                            d=int(input("Select"))
                            match d:
                                case 1:
                                    for i in range(5):
                                        a=float(input("enter score for math"))
                                        math_li.append(a)
                                        save_data()
                                    print("scores added succesfully")
                                case 2:
                                    for i in range(5):
                                        a=float(input("enter score for english"))
                                        english_li.append(a)
                                        save_data()
                                    print("scores added succesfully")
                                case 3:
                                    for i in range(5):
                                        a=float(input("enter score for physics"))
                                        physics_li.append(a)
                                        save_data()
                                    print("scores added succesfully")
                                case 4:
                                    for i in range(5):
                                        a=float(input("enter score for chemistry"))
                                        chemistry_li.append(a)
                                        save_data()
                                    print("scores added succesfully")
                                case 5:
                                    for i in ramge(5):
                                        a=float(input("enter score for art"))
                                        art_li.append(a)
                                        save_data()
                                    print("scores added succesfully")
                            
                        case 2:
                            print("Select subject to delete the score")
                            print("1)Math🔢")
                            print("2)English🦋")
                            print("3)Physics🌍")
                            print("4)Chemistry👩‍🔬")
                            print("5)Art✏️")
                            p=int(input("Select"))
                            match p:
                                case 1:
                                    math_li.clear()
                                    save_data()
                                    print("score deleted succesfully")
                                case 2:
                                    english_li.clear()
                                    save_data()
                                    print("score deleted succesfully")
                                case 3:
                                    physics_li.clear()
                                    save_data()
                                    print("score deleted succesfully")
                                case 4:
                                    chemistry_li.clear()
                                    save_data()
                                    print("score deleted succesfully")
                                case 5:
                                    art_li.clear()
                                    save_data()
                                    print("score deleted succesfully")
                        case 3:
                            print("Select subject to avereage the score")
                            print("1)Math🔢")
                            print("2)English🦋")
                            print("3)Physics🌍")
                            print("4)Chemistry👩‍🔬")
                            print("5)Art✏️")
                            q=int(input("Select"))
                            match q:
                                case 1:
                                    if len (math_li)>0:
                                        a=sum(math_li)/len (math_li)
                                        print(a)
                                        print("average is ready")
                                case 2:
                                    if len (english_li)>0:
                                        a=sum(english_li)/len (english_li)
                                        print(a)
                                        print("average is ready")
                                case 3:
                                    if len (physics_li)>0:
                                        a=sum(physics_li)/len (physics_li)
                                        print(a)
                                        print("average is ready")
                                case 4:
                                    if len (chemistry_li)>0:
                                        a=sum(chemistry_li)/len (chemistry_li)
                                        print(a)
                                        print("average is ready") 
                                case 5:
                                    if len (art_li)>0:
                                        a=sum(art_li)/len (art_li)
                                        print(a)
                                        print("average is ready")  
                        case 4:
                            print("Select subject to see the best and worst score")
                            print("1)Math🔢")
                            print("2)English🦋")
                            print("3)Physics🌍")
                            print("4)Chemistry👩‍🔬")
                            print("5)Art✏️")
                            f=int(input("Select"))
                            match f:
                                case 1:
                                    if math_li:
                                        print("best",max(math_li))
                                        print("worst",min(math_li))
                                    
                                case 2:
                                    print("best",max(english_li))
                                    print("worst",min(english_li))

                                case 3:
                                    print("best",max(physics_li))
                                    print("worst",min(physics_li))

                                case 4:
                                    print("best",max(chemistry_li))
                                    print("worst",min(chemistry_li))

                                case 5:
                                    print("best",max(art_li))
                                    print("worst",min(art_li))

        case 2:
            exit()
            print("goodbye💫💕")  
            




                    
