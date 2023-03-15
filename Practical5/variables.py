a=-3.19 #Store the longitude of Edinburgh
b=-118.24 #Store the longitude of Los Angeles
c=116.39 #Store the longitude of Haining
d=abs(a-b) #Caculate the distance between Los Angeles and Edinburgh
e=abs(a-c) #Caculate the distance between Haining and Edinburgh
if (d>e): #Compare d and e which is bigger
 print("d is greater,Rob travelled further to Los Angeles.")
else:
 print("e is greater,Rob travelled further to Haining")
  #Answer:e is greater, Rob travelled further to Haining.
  X=True
Y=False
W=X and Y
Z=X or Y
print(W)#the answer is False
print(Z)#the answer is True
