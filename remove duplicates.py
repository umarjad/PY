def remove_duplicates_and_sort(input_str):
    # Split the input string into words
    words = input_str.split()

    # Remove duplicates by converting the list of words into a set
    unique_words = set(words)

    # Sort the unique words alphabetically
    sorted_words = sorted(unique_words)

    # Join the sorted words into a string separated by whitespace
    result = ' '.join(sorted_words)

    return result

# Example usage:
input_str = "hello world and practice makes perfect and hello world again"
output = remove_duplicates_and_sort(input_str)
print("Output:", output)
