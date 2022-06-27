my_file=open(" question3.txt ","r")
for i in my_file:
    if "delhi" in i:
        x=open( "delhi.txt","a")
        x.write(i)
        x.close()
    elif "shimla" in i:
        y=open("shimla.txt","a")
        y.write(i)
        y.close()
    else:
        z=open( "others.txt" ,"a")
        z.write(i)
        z.close()
my_file.close()
