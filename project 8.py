# #PROJECT 8 
# #word frequency counter- reads a passege counts how often each word appears using a dictionary display top 5 most frequent words using stored()+comprehensions
a=(input("enter a passage:---"))
b=a.lower().split()
freq={}
for i in b:
    freq[i]=freq.get(i,0)+1
sort=sorted(freq.items())
print("\n Top 5 most repitive words are")
for i in range(min(5,len(sort))):
    print(sort[i])