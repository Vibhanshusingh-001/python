# os me jo cheej manually karte hai use automate kar sakte h
# operating system ke bahut saare opration perform karne me madad karta h
# koi bhi cheej automate karni ho to os module ka use karte h
# bulk  operations kar sakte ho like folder rename kar sakte ho , folder create kar sakte ho, read kr sakte ho
import os
if(not os.path.exists("data")): #ye isliye bana rahe hai kyuki data file already exist kar rhi h
 os.mkdir("data")
for i in range(0,100):
    os.mkdir(f"data/day{i+1}")#data ke andar har day ka folder ban jaaye
# import os
# for i in range (0,100):
#     os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")
#data ke ander kon kon se folder hain
# import os
# folders=os.listdir("data")
# # print(folders)
# # for folder in folders:
# #     print(folder)
# # for folder in folders:
# #     print(folder)
# #     print(os.listdir(f"data/{folder}"))
# os.chdir("/users")
# print(os.getcwd())#to know current directory
