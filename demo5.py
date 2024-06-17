def greet(name,age):
    print("Hello, " + name+"! You are",+ str(age) +"years old.")
    
    person = ["Vaishnavi",20]
    greet(*person)
   