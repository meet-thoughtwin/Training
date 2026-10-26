#method/function overloading = same method name but different params(not supported in python)


class Calculator:
    
    # 1st add method(two params)
    def add(self,a,b):
        return a+b
    
    # 2nd add method(three params)
    def add(self,a,b,c):
        return a+b+c


#creating object 
adding= Calculator()

# calling method 1
print(adding.add(10,20)) # gives type error one argument is missing

#calling method 2
print(adding.add(10,20,30)) # output - 60


# note = python does not support true method overloading 
#        bcz 2nd method replaces the 1st method, this is method overloading