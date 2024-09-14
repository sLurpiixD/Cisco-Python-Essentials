beatles = []
print("Step 1:", beatles)

beatles.append('John Lennon') 
beatles.append('Paul McCartney') 
beatles.append('George Harrison')
print("Step 2:", beatles)

for member in ['Stu Sutcliffe','Pete Best']:
    beatles.append(member)
print("Step 3:", beatles)

del beatles[-1] # Since, in Step 3, it added 2 more names. It must be noted that adding something in a list is simply placing it at the last part.
del beatles[-1]
print("Step 4:", beatles)

beatles.insert(0, 'Ringo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

