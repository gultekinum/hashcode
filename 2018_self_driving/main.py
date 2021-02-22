import sys

file_dict = {
1:["a_example.in","a_submission.in"],
2:["b_should_be_easy.in","b_submission.in"],
3:["c_no_hurry.in","c_submission.in"],
4:["d_metropolis.in","d_submission.in"],
5:["e_high_bonus.in","e_submission.in"]
}

class Drive:
    def __init__(self,line,id):
        for i in range(len(line)):
            line[i]=int(line[i])
        self.id = id
        self.source=line[0:2]
        self.destination=line[2:4]
        self.es = line[4]
        self.lf = line[5]
        self.distance = self.calculate_distance()
    def calculate_distance(self):
        return abs(self.source[1]-self.destination[1])+abs(self.destination[0]-self.source[0])

class Car:
    def __init__(self):
        self.drives = []
        self.step = 0
        self.last_position=[0,0]
    def increase_step(self,inc):
        self.step +=inc


def read_data(fname):
    f = open(fname,"r")
    info = f.readline().strip().split()
    drives = []
    count = 0
    for x in f:
        drives.append(Drive(x.strip().split(),count))
        count+=1
    return info,drives

def calculate_distance(coor1,coor2):
    return abs(coor1[1]-coor2[1])+abs(coor1[0]-coor2[0])

file_choice = int(sys.argv[1])

res = read_data(file_dict[file_choice][0])
info = res[0]
drives = res[1]
car_count = int(info[2])
step_count = int(info[5])

drives = sorted(drives, key=lambda x: x.es, reverse=False)
# for items in drives:
#     print (items.source,items.destination,items.es,items.lf,items.distance)

cars = []
for i in range(car_count):
    cars.append(Car())

for a in range(len(cars)):
    while drives:
        moved_step = calculate_distance(cars[a].last_position,drives[0].source)
        total_step = cars[a].step+drives[0].distance+moved_step
        if total_step>step_count:
            break
        print("adding,"+str(drives[0].id))
        cars[a].last_position = drives[0].destination
        cars[a].drives.append(drives[0].id)
        cars[a].increase_step(drives[0].distance)
        drives.pop(0)
result = ""
for car in cars:
    drive_result =' '.join(str(e) for e in car.drives)
    drive_result = str(len(car.drives))+" "+drive_result
    result=result+drive_result+"\n"
    print(drive_result)
f = open(file_dict[file_choice][1],"w")
f.write(result)





