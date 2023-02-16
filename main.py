# # remember to fork this and push to github
# f = open('test.txt', 'r')
# # it opens the file and r = reading mode
# print(f.read())
# # read() reads everthing, all of the lines
# # readline() reads onlt the first line
# #  computer is in reading mode and we call it to read
# f.close()
# # closes file

# f = open('test.txt', 'w')
# f.write("Gosh, this")
# f.close()
# # W overrides the text
# # A adds text

# with open("test.txt", "w") as f: #This is called a conetxt manager
#   f.write("gjgjgjgjgjgjgjgjgjgj")
#   print(f)

# with open("test.txt", "r") as f: #This is called a conetxt manager
#   # f_contents = f.read()
#   # print(f_contents)

# with open("test.txt", "r") as f:
#   for line in f:
#     # print(line,end='') Prints text

with open("period7.txt", "w") as f:
  f.write("this mess is over")