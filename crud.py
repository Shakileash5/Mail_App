import csv
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
  
  
# name of csv file 
filename = "user.csv"
data = []
  
# writing to csv file 
def read_data():
    with open(filename, 'r',) as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row not in data:
                data.append(row)
    print(data)
    return 
        # writing the data rows 


def writeData(uname,mail,password):

    for i in data:
        if i[1] == mail:
            return -1

    if [uname,mail,password] not in data:
        data.append([uname,mail,password])
        print(data)
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([uname,mail,password])
            #for i in data:
            #    writer.writerow(i)
#read_data()
#writeData("shakiladawd3","feaawad","atshaya123")

def update(uname,mail,password):
    for i in data:
        if mail == i[1]:
            i[2] = password
            #i[0] = ",".join(datas)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in data:
            writer.writerow(i)


            

#update("shakiladawd3","feaawad","atshaya1243")

