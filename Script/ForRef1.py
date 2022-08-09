fileName = "G:\\My Drive\\_Documents\\_Read\\_Paper\\Crop Science\\2016\\56\\5\\P2731\\ref1.txt"
f = open(fileName, "r")

imsi = f.readline()
print(imsi.split("//")[1] )

print(f.readline())
print(f.read(100))