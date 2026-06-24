# PROJECT 2 WORD COUNTER AND ANALYZER
para=input("Enter a paragraph:--")
count=0
for ch in para:
    count+=1
print("Number of characters:-",count)

vowel_count=0
for i in para:
    if i in "aeiou":
        vowel_count+=1
        print("The number of vowels are:-",vowel_count)

words = para.split()
longest = words[0]

for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word is:-", longest)



