file1 = open("/home/gobi/Desktop/8085OPCodeGenerator/db.txt","r+")
file2 = open("/home/gobi/Desktop/8085OPCodeGenerator/db1.txt","w+")

for line in file1:
    new = line.split(" ")