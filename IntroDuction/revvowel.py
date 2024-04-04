def reverse_vowels(input_str):
    vowels = 'AEIOUaeio'
    input_str = list(input_str)
    vowel_positions = [i for i, char in enumerate(input_str) if char in vowels]
    reversed_vowels = [input_str[i] for i in reversed(vowel_positions)]
    # Replace the vowels in the string with the reversed vowels
    for i, pos in enumerate(vowel_positions):
        input_str[pos] = reversed_vowels[i]
    
    return ''.join(input_str)

# Example usage:
input_str = "rAmoNu"
result = reverse_vowels(input_str)
print(result)
