def generate_sequential_number_strings(length, num_strings, filename="sequential_number_strings.txt"):
    with open(filename, "w") as file:
        i = 10000000
        for i in range(num_strings):
            # Format the number to be length characters long, filled with zeros
            number_string = f"{i:0{length}d}"
            # Write the formatted string to the file
            file.write(number_string + '\n')

# Example usage: generate 10 sequential strings starting from '00000000'
generate_sequential_number_strings(8, 100000000)