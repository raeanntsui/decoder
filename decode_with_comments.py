def decode(message_file: str) -> str:
    with open(message_file, "r") as file:
        lines = file.readlines()
        separated_lines = sorted(lines, key=lambda string:int(string.split()[0]))
        refined_separated_lines = [item.strip() for item in separated_lines]
 
        # print("refined_separated_lines", refined_separated_lines)
        # refined_separated_lines => ['1 down', '2 each', '3 dont']

        line_code_dict = {}
        for item in refined_separated_lines: 
            key, value = item.split()
            line_code_dict[int(key)] = value

        # print("line code dict", line_code_dict)
        # line_code_dict => {1: 'down', 2: 'each', 3: 'dont'}

        size = len(line_code_dict) # determine length of line_code_dict => 300
        target_words_arr = []

        row = 1
        current_last_index = 1
        while current_last_index < size:
            """
            1            row 1, last_index = 1 down
            2 3          row 2, last_index = 3  (1 + row 2) dont
            4 5 6        row 3, last_index = 6  (3 + row 3) nine
            7 8 9 10     row 4, last_index = 10 (6 + row 4) lot
            """
            target_words_arr.append(line_code_dict[current_last_index])
            row += 1
            current_last_index += row

        if current_last_index == size:
            target_words_arr.append(line_code_dict[current_last_index])
        else:
            # case where pyramid does not fill all the way up in the last row
            # we can add the last digit of the row
            target_words_arr.append(line_code_dict[size])

        # print("target array before join", target_words_arr) 
        # ['down', 'dont', 'nine', ...]
        return " ".join(target_words_arr) 
print(decode("coding_qual_input.txt"))