import sqlite3

file1 = open("/home/gobi/Desktop/8085OPCodeGenerator/db.txt","r+")
file2 = open("/home/gobi/Desktop/8085OPCodeGenerator/db1.txt","w+")

database = sqlite3.connect("OPCodes.db")
db = database.cursor()

# for line in file1:
#     temp = []
#     words = line.split(" ")
#     temp.append(words[0])
#     temp.append(" ".join(words[1:-2]))
#     temp.append(words[-2])

    # db.execute("Insert into OPCodes (Size,Instruction,OPCode) VALUES (?,?,?)",temp)

for row in db.execute("SELECT * FROM OPCodes"):
    print(row)

database.commit()    
file1.close()
file2.close()