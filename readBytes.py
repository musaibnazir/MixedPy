print("Welcome To The File Copying Program")
stream=open("image.png","rb")
str=stream.read()
stream.close()
#print(str)
other = open("/home/mnr/Desktop/newfile.png","wb")
other.write(str)

print("File Copied")
