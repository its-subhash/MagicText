text="""Hello this is subhash
and am writing this text to% &&&   ** *) )) ## #?  ??/ //   test     my operations      if it works or      not
and this is a new line to check other things"""

#Uppercase
Uppercase= text.upper()
print ("1)  for upper case : ", Uppercase)

#Lowercase
Lowercase =text.lower()
print ("2)  for lower case : ", Lowercase)

#for Removing all punctuations
punctuations="~!@#$%^&*()_+=|?\/><"
Analyzed =""
for char in text:
    if char not in  punctuations:
        Analyzed = Analyzed + char
print("3)  for punctuations case : ",Analyzed)


#for extra space removal
spaceremoved=""
for index, char in enumerate (Analyzed):
    if not(Analyzed[index]== " " and Analyzed[index+1]==" "):
        spaceremoved = spaceremoved + char
print("4)  for Extra space removal : ",spaceremoved)

#WORD COUNT

wordreplaced=spaceremoved
wordscount=len(spaceremoved.split())
print(wordscount)

#for replacement
replace="is"
by="hello"
i=wordreplaced.replace(f" {replace} ", f" {by} ")
print(i)