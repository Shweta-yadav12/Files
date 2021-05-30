# Courses
# Login/Signup
# Question 3

# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line
#  mein daalo. Aapki list yeh rahi:
 
banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"] 
# for i in banks_list:
f=open("people3.txt","w")
i=0
while i<len(banks_list):
    f.write(banks_list[i])
    f.write("\n")
    i=i+1