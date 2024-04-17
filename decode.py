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
        else:
            target_words_arr.append(line_code_dict[size])

        return " ".join(target_words_arr) 
print(decode("coding_qual_input.txt"))