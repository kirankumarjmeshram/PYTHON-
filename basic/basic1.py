# User Input: The input() function allows user input. 
# It takes the line entered on a console and convert it into a string & returns it

# fname = input('Fname: ')
# print(fname)


a = [1,2,3,4,5,6,7,8,9]

print(a[0:4]) #[1, 2, 3, 4] 
print(a[0:7:2]) #[start:stop:step] # [1, 3, 5, 7]
print(a[0:7:1]) # [1, 2, 3, 4, 5, 6, 7]
print(a[4:2:-1]) # [5,4]
print(a[::-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1]