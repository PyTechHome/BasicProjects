# String Concatination

#youtuber="Jacky Chan"

#print("Subscribe to " + youtuber)
#print("Subscribe to {}".format(youtuber))
#print(f"Subscribe to {youtuber}")

adjective=input("Enter an Adjective: ")
gadget=input("Enter a Gadget: ")
verbing=input("Enter a verb --ing: ")
robject=input("Enter a name of an object: ")
funny_word=input("Enter a form of energy: ")

madlib=f"""\nThe Tech Glitch\n 
One {adjective} morning, I turned on my {gadget} and it started {verbing}!\n  
So I grabbed a {robject} and fixed it myself. Now everything runs on {funny_word} power!\n\n"""
print(madlib)