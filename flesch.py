def count_syllables(word):
    count = 0
    vowels = "aeiouy"
    if len(word) <= 3:
        count = 1
    else:
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
    return count

def calculate_flesch_index(text):
    words = text.split()
    sentences = text.split(". ") 

    total_syllables = sum(count_syllables(word) for word in words)
    average_syllables_per_word = total_syllables / len(words)
    average_words_per_sentence = len(words) / len(sentences)

    flesch_index = 206.835 - (1.015 * average_words_per_sentence) - (84.6 * average_syllables_per_word)
    grade_level = 0.39 * average_words_per_sentence + 11.8 * average_syllables_per_word - 15.59

    return flesch_index, grade_level


    
file = open("flesch.txt", "r")
text = file.read()
flesch_index, grade_level = calculate_flesch_index(text)

print(f"Flesch Index: {flesch_index}")
print(f"Grade Level: {grade_level}")

