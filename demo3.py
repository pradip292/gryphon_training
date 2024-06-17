def greet(name, age):
    print(f"Hello {name}, you are {age} years old")
    
    
people = [
      {'name': 'John', 'age':25},
      {'name': 'John1', 'age':25},
      {'name': 'John2', 'age':25},
      {'name': 'John3', 'age':25}]
for i in people:
      greet(i['name'], i['age'])
      print(i)
      

def greet1(address,pin):
    print(f"Hello {address}, your pin is {pin}")
    
demo = [
    {'address': 'Pune', 'pin':423601},
     {'address': 'mumbai', 'pin':423601},
      {'address': 'Pune', 'pin':423601}
]
for i in demo:
    greet1(i['address'], i['pin'])
    print(i)
 

