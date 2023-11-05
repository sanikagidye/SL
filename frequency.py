plain_text=input("Enter plain text:")

def calculate_frequency(text):
    letter_count={}
    total_count=0
    for char in text:
        if char.isalpha():
            char=char.lower()
            letter_count[char]=letter_count.get(char,0)+1
            total_count+=1
    frequency_percentage={}
    
    for letter,count in letter_count.items():
        percentage = (count/total_count)*100
        frequency_percentage[letter]=round(percentage,2)
    return frequency_percentage
    
frequency_analysis=calculate_frequency(plain_text)
for letter,percentage in frequency_analysis.items():
    print("{}:{}%".format(letter,percentage))
