#file = open("Buildings_000001.txt")

with open("Buildings_000001.txt","r") as f: 
    master_file = open("three_buildings.txt","w")
    master_file.write(f.readline())
    master_file.close()

print("Finished adding header")

for i in range(3,7):
    file_name = "Buildings_0000" + str(i).zfill(2) + ".txt"
    new_file = open("three_buildings", "a+")
    with open(file_name, "r") as data:
        data.readline() #read header  
        new_file.write(data.read())

    new_file.close()

print("Done adding")

#The file sizing is does not match
