import string

# most common letters (single)
letter_frequencies = {
    'A':  8.55,                
    'B':  1.60,               
    'C':  3.16,               
    'D':  3.87,               
    'E': 12.10,             
    'F':  2.18,            
    'G':  2.09,                    
    'H':  4.96,                      
    'I':  7.33,                        
    'J':  0.22,        
    'K':  0.81,        
    'L':  4.21,       
    'M':  2.53,        
    'N':  7.17,        
    'O':  7.47,        
    'P':  2.07,        
    'Q':  0.10,                 
    'R':  6.33,                 
    'S':  6.73,                 
    'T':  8.94,  
    'U':  2.68,
    'V': 1.06,
    'W':  1.83,
    'X':  0.19,
    'Y':  1.72,
    'Z':  0.11   
}

# most common double letters
common_doubles = ["ss", "ee", "tt", "ff", "ll", "mm", "oo"]

# most common single most_common_words
common_singles = ['a', 'I']

# most common pairs of letters that aren't necessarily words and that are not both the same
common_pairs = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 'en', 'es', 'of', 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've']

# most common two letter words
common_pair_words = ['of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am']

# most common triples of letters that aren't words
trigrams = ['the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men']

# most frequent initial letters in a word
common_initials = ['T', 'O', 'A', 'W', 'B', 'C', 'D', 'S', 'F', 'M', 'R', 'H', 'I', 'Y', 'E', 'G', 'L', 'N', 'P', 'U', 'J', 'K']

def score(result):
    score = 0
    words = result.split()
    
    for word in words:
        for letter in letter_frequencies:
            if letter.lower() in word:
                score += letter_frequencies[letter]
        if word[0][0] in common_initials and word[0][0].isupper():
            score += 20
        for double in common_doubles:
            if double in word:
                score +=20
        for pair in common_pairs:
            if pair in word:
                score +=20
        for pair_word in common_pair_words:
            if pair_word in word:
                score +=20
        for trigram in trigrams:
            if trigram in word:
                score +=20
    return score

# examine the frequency of each xor result to find best scoring match
def find_match(results):
    highest_score = 0 
    for i, result in enumerate(results):
        result_to_string = ''.join(result)
        if score(result_to_string) > highest_score:
            highest_score = score(result_to_string)
            key = i
            plaintext = result_to_string
    return (highest_score, key, plaintext)