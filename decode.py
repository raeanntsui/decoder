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
        while current_last_index <= size:
            target_words_arr.append(line_code_dict[current_last_index])
            row += 1
            current_last_index += row

        return " ".join(target_words_arr) 
print(decode("coding_qual_input.txt"))


#! CODE EXPLAINED BELOW

# This function, called 'decode', processes and deciphers a hidden message stored in a given text file. Decoding the message requires the construction of a hypothetical pyramid where only the last word of each row of the pyramid will be extracted while all other words are disregarded. 

# The function begins by opening the 'message_file' which contains an unsorted list of words. The file is then read into memory as a list for further processing. To organize the data effectively, 'separated_lines' sorts the lines based on a numerical value found at the beginning of each line. This is particularly useful because now the lines of text with numbers at the beginning are now sorted in ascending order from least to greatest. After sorting, 'refined_separated_lines' stores the lines without any leading or trailing whitespace to enhance readability. This list serves as a foundational component for later iteration using a while loop. Using a while loop in this case instead of a for loop offers flexibility when the number of iterations is not predetermined. In the decoding process, the number of iterations depends on the structure of the message and its decoding pattern, which may vary.

# Before initiating the while loop, a dictionary called 'line_code_dict' is created to enhance efficiency for lookup by pairing line numbers with associated words using key-value pairs. Additionally, the function determines the maximum size of the dictionary which would be used to dictate the stopping point for the while loop. In this particular instance, the stopping point will be at 300 words. Initialization of an empty list 'last_values' acts as a placeholder for the chosen decoded words.

# The core logic of the ‘decode’ function involves building each tier of the pyramid line by line using a while loop. Within this loop, each iteration corresponds to a new row in the pyramid structure with each successive row expanding by one unit. The construction of the pyramid starts from its apex so the first row is initialized to 1 and 'current_last_index' is also initialized to 1. 'current_last_index' represents the position (or index) of the last word in each row. At this point, the last word of each row will be appended to 'target_words_arr'. To continue the loop, the 'row' increases by 1 and 'current_last_index' increases by the updated value of row. Finally, the function joins the elements of 'target_words_arr' array as a string.
