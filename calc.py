# Minimal script to test unit testing
# From tutorial: https://www.youtube.com/watch?v=6tNS--WetLI

def add(x, y):
   """Add Function"""
   return x + y

def subtract(x, y):
   """Subtract Function"""
   return x - y

def multiply(x, y):
   """Multiply Function"""
   return x * y

def divide(x, y):
   """Divide Function"""
   if y == 0:
      raise ValueError('Cannot divide by zero!')
   return x / y

print('Hello from calc!')
print('1 + 1 = '+str(add(1,1)))
print('1 - 1 = '+str(subtract(1,1)))

# Export to csv
ofile = open("log.txt","w")  
ofile.write("Executed successfully!")
ofile.close() 