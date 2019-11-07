with open("input.txt") as fp:
    file_contents = fp.read()

#AoC 2018.1

t2 = file_contents.split('\n')
a=0
for i in t2[:-1]:
	a=a+int(i)



print(a)
#Jo megoldas!
