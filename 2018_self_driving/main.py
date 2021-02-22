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
        return abs(self.source[1]-self.source[0])+abs(self.destination[0]-self.destination[1])

class Car:
    def __init__(self):
        self.drives = []
        self.step = 0
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
print("helloo")
file_choice = int(sys.argv[1])

res = read_data(file_dict[file_choice][0])
info = res[0]
drives = res[1]
car_count = int(info[2])
step_count = int(info[5])

drives = sorted(drives, key=lambda x: x.es, reverse=False)
for items in drives:
    print (items.source,items.destination,items.es,items.lf,items.distance)
# cars = []
# for i in range(car_count):
#     cars.append(Car())


