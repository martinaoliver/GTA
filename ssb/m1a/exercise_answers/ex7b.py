months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August',9:'September', 10:'October', 11:'November', 12:'December'}    

m = int(input("Enter a number between 1 and 12: "))
print ("The month for", m, "is", months[m])

# You could improve this code by printing an error message if an
# incorrect number is entered (<1 or >12)
