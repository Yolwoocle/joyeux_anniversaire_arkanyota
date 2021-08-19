import os

for r, d, f in os.walk("./notes"):
    print(r, d, f)


path = "/home/ay/Cours2022Git"
data = [os.path.join(path+"/notes", f).split("/")[-1] for f in os.listdir(path+"/notes") if os.path.isdir(os.path.join(path+"/notes", f))]
print(data)

cp = 0
for j in range(5):
    print(j, "Hello", [(i+j)%5 for i in range(4,-1, -1)])
