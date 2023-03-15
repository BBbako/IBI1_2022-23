#Store the longitude of Edinburgh，Los Angeles and Haining.
a=-3.19  
b=-118.24 
c=116.39 
#Caculate the distance between Los Angeles and Edinburgh
d=abs(a-b) 
#Caculate the distance between Haining and Edinburgh
e=abs(a-c) 
#Compare d and e which is bigger
if (d>e): 
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
