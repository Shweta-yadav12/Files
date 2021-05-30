# tion 4

# Iss text ko question3.txt ke naam ki file mein save karo. Iss file mein dhyaan se dekhoge toh ek 
# insaan ka naam aur ek sheher ka naam milegaYeh sheher woh sheher hai jisme woh insaaan rehta hai. Ab 
# aapne ek aisa code likhna hai jo: 1. Delhi mein rehne waale logon ko ek alag file mein daale. Delhi 
# waali file ka naam "delhi.txt" hona chaiye. 2. Shimla mein rehne waale logon ko ek alag file mein
#  daale. Shimla waali file na naam "shimla.txt" hona chaiye 3. Aur saare log jo delhi aur shimla mein 
#  nahi rehte, unko ek alag file mein daale. Iss file ka naam "others.txt" hona chaiye

# Aapko aisa code likhna hai, jo aisi file mein kitni bhi lines pe chal paye.


# f=open("people4.txt,r")
# file=open("pepole-txt","r")
# for i in (file):
#     if "delhi" in i:
#         file=open("delhi.txt","a")
#         file.write(i)
#     elif "shimla" in i:
#         file=open("shimla.txt","a")
#         file.write(i)
#     else:
#         file=open("others.text","a")
#         file.write(i)
#     i=i+1
# file.close()

my_file=open("people4.txt","w")
file_data=my_file.write("life is not about finding your is all about yourself")
a_name=open("people4.txt","r")
name_data=a_name.read()
print(name_data)