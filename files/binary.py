# Opening the binary file in binary mode as rb(read binary)
f = open("NotoSansShavian-Regular.bin", mode="rb")
 
# Reading file data with read() method
data = f.read()
 
# Knowing the Type of our data
print(type(data))
 
# Printing our byte sequenced data 
print(data)
 
# Closing the opened file
f.close()


# #######################

# Specify the size of each chunk to read
chunk_size = 10

file = open("NotoSansShavian-Regular.bin", "rb")
# Using while loop to iterate the file data
while True:
	chunk = file.read(chunk_size)
	if not chunk:
		break
	# Processing the chunk of binary data
	print(f"Read {len(chunk)} bytes: {chunk}")



