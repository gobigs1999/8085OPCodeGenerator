import sqlite3

file1 = open("/home/gobi/Desktop/8085OPCodeGenerator/input.txt","r+")
file2 = open("/home/gobi/Desktop/8085OPCodeGenerator/output.txt","w+")

database = sqlite3.connect("OPCodes.db")
db = database.cursor()

for line in file1:
    line=line.split()
    print(line[0])
    row = db.execute("SELECT * FROM OPCodes WHERE Instruction LIKE '?%'",line[0])
    print(row)

database.commit()    
file1.close()
file2.close()