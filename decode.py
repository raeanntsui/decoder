def decode(message_file: str) -> str:
    with open(message_file, "r") as file:
        lines = file.readlines()
        separated_lines = sorted(lines, key=lambda string:int(string.split()[0]))
        refined_separated_lines = [item.strip() for item in separated_lines]

        line_code_dict = {}
        for item in refined_separated_lines: 
            key, value = item.split()
            line_code_dict[int(key)] = value

        size = len(line_code_dict)
        target_words_arr = []

        row = 1
        current_last_index = 1
        while current_last_index < size:
            target_words_arr.append(line_code_dict[current_last_index])
            row += 1
            current_last_index += row

        if current_last_index == size:
            target_words_arr.append(line_code_dict[current_last_index])
        # else:
        #     target_words_arr.append(line_code_dict[size])

        return " ".join(target_words_arr) 
print(decode("coding_qual_input.txt"))

# This function, called 'decode', processes and deciphers a hidden message stored in a given text file. Decoding the message requires the construction of a hypothetical pyramid where only the last word of each row of the pyramid will be extracted while all other words are disregarded. 

# The function begins by opening the 'message_file' which contains an unsorted list of words. The file is then read into memory as a list for further processing. To organize the data effectively, 'separated_lines' sorts the lines based on a numerical value found at the beginning of each line. This value, extracted by a lambda function, ensures proper sorting for subsequent steps particularly when using a while loop for decoding. This is particularly useful because now the lines of text with numbers at the beginning are now sorted in ascending order from least to greatest which is necessary when building a pyramid from scratch. After sorting, 'refined_separated_lines' stores the lines without any leading or trailing whitespace, enhancing readability. This list serves as a foundational component for later iteration using a while loop. Using a while loop in this case instead of a for loop offers flexibility when the number of iterations is not predetermined. In the decoding process, the number of iterations depends on the structure of the message and its decoding pattern, which may vary.

# Before initiating the while loop, a dictionary called 'line_code_dict' is created to enhance efficiency for lookup by pairing line numbers with associated words using key-value pairs. Additionally, the function determines the maximum size of the dictionary which would be used as the future while loop's stopping point. In this particular instance, the stopping point will be at 300 words. Initialization of an empty list 'last_values' acts as a placeholder for the chosen decoded words.

# The core logic of the ‘decode’ function involves building each tier of the pyramid line by line using a while loop. Within this loop, each iteration corresponds to a new row in the pyramid structure with each successive row expanding by one unit. The construction of the pyramid starts from its apex so the starting point with the row counter is set to 1 and the 'current_last_index' is also initialized to 1. On each iteration, the row counter increments by 1 and 'current_last_index' increases by the sum of the new row number and the previous loop's 'current_last_index' value. Decoded words from each iteration are appended to 'target_words_arr'. At the end of each round of the while loop, the function checks whether 'current_last_index' matches the size of the dictionary. If 'current_last_index' equals 'size', the function appends the corresponding word at the ‘current_last_index’. Finally, the function joins the elements of 'target_words_arr' with spaces and returns the decoded message as a string.

