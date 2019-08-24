#Function definition:
def lim_text(tex,l):
    inp = tex.read() 
    x=len(inp) #Checking the length/number of characters of the input file 
    i=0         
    imax=i+l   #Limiting the max length of the line  
    while i <= x:
       if inp[imax] == ' ' or inp[imax] == '.':   #Checking out the last character of the line in order not to breake words
           print(inp[i:imax])
           i=imax+1
           imax=i+l
           if imax > x:
               imax=x
               print(inp[i:imax])     #Printing the line according to the conditions
               i=imax+1
       else:
           imax=imax-1        
           continue

solution = lim_text(open('text.txt'),40)   #Calling the function to rewrite the file 'text.twt' with maximum 40 characters per line.


