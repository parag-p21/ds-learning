Cubes=[n*n*n for n in range(1,11)]
print(Cubes)


Div=[d for d in range (1,51) if d % 3==0 and d % 5==0]
print(Div)

Sent="Data Science and Machine Learning"
vowels = [char for char in Sent if char.lower() in 'aeiou']
print(vowels)

#QS2
students = {"Riya": 87, "Aman": 35, "Parag": 92, "Neha": 28, "Dev": 76}
passed = {name: marks for name, marks in students.items() if marks >= 40}
print(passed)

grades = {
    name: ('A' if marks >= 75 else 'B' if marks >= 50 else 'C')
    for name, marks in students.items()
}
print(grades)

#Qs3
prices = ["₹299", "₹599", "N/A", "₹199", "N/A", "₹899", "INVALID", "₹149"]
valid_prices = [int(p[1:]) for p in prices if p.startswith("₹")]
print(valid_prices)
print("Min:", min(valid_prices))
print("Max:", max(valid_prices))
print(f"Average: ₹{sum(valid_prices)/len(valid_prices):.2f}")



 #Qs4
sentences = [
    "Data Science is amazing",
    "Python is powerful",
    "Machine Learning is the future",
    "AI and Data Science will change the world"
]

#
print(len(sentences[0].split()))    # 4

word_counts = [len(s.split()) for s in sentences]
print(word_counts)
data_sentences = [s for s in sentences if "Data" in s]
print(data_sentences)

unique_words = {word.lower() for s in sentences for word in s.split()}
print(unique_words)
print(sorted(unique_words))