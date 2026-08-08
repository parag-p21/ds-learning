text="  data science with python  "
print(text.upper())
print(text.title())
print(text.lower())
print(text.strip())
print(text.replace("python","Pandas"))

print(len(text.split()))

text1="Parag,19,Balaghat,CS,87.5"
Data=text1.split(",")
name=Data[0]
marks=Data[4]
city=Data[2]
age=Data[1]
branch=Data[3]
print(f"Name: {name}, Marks: {marks} City:{city} Branch:{branch} Age:{age}")

#Fun that strips,lowers and remove commas
def clean_text(text):
    return text.strip().lower().replace(",","")
print(clean_text("  Hello, World, Data Science,  "))

#
def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
print(is_palindrome("racecar"))    # True
print(is_palindrome("Madam"))     # True
print(is_palindrome("Data Science"))


#takes a paragraph of text and returns a dictionary with:

def word_stats(text):
    words=text.split()
    words_count=len(words)
    unique_words=len(set(words))
    longest_word=max(words,key=len)
    avg_word_length = round(sum(len(w) for w in words) / len(words), 2)

    return{
        "word_count":words_count,
        "unique_words":unique_words,
        "longest_word":longest_word,
        "avg_word_length ":avg_word_length



    }
print(word_stats("data science is the study of data and science and the art of analysis"))