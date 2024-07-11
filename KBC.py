questions=[["who is the king of forest","lion","tiger","dog","cat",1],["who is the king of forest","lion","tiger","dog","cat",1],
           ["who is the king of forest","lion","tiger","dog","cat",1],["who is the king of forest","lion","tiger","dog","cat",1]
           ,["who is the king of forest","lion","tiger","dog","cat",1],["who is the king of forest","lion","tiger","dog","cat",1],
           ["who is the king of forest","lion","tiger","dog","cat",1],["who is the king of forest","lion","tiger","dog","cat",1],
           ["who is the king of forest","lion","tiger","dog","cat",1]]
levels=[1000,2000,6000,10000,50000,80000]
money=0
for i in range (0,len(questions)):
    question=questions[i]
    print(f"\n\n question for rupees  :{levels[i]}")
    print(f"{question[0]}")
    print(f"a.{question [1]}               b.{question [2]}")
    print(f"c.{question [3]}               d.{question [4 ]}")
    reply=int (input("enter your answer between 1-4 or 0 to quit\n"))
    if reply==0:
        money=levels[i-1]
        break
    if reply==question[-1]:
        print(f"correct answer you won{levels[i]} ")
        if i==4:
            money=50000
        elif i==5:
            money=80000
    else:
            print("wrong answer")
            break
print(f"your money take home is {money}")





