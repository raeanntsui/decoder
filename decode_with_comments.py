def decode(message_file):
    with open("coding_qual_input.txt", "r") as file:
        lines = file.readlines()
        # print(lines)

        sorted_lines = sorted(lines, key=lambda string:int(string.split()[0]))
        # print(sorted_lines)

        # remove the /n from each item in the sorted_lines array
        refined_sorted_lines = [item.strip() for item in sorted_lines]
        # print(refined_sorted_lines)

        sorted_lines_object = {}
        for item in refined_sorted_lines: 
            key, value = item.split()
            sorted_lines_object[int(key)] = value
        print(sorted_lines_object)
            
        # print("length of the object", len(sorted_lines_object))
        step = 2
        start_point = 1
        end_point = len(sorted_lines_object)
        keys_to_select = range(start_point, end_point + 1, step)
        result = ' '.join(sorted_lines_object[key] for key in keys_to_select)
        print(result)


decode("coding_qual_input.txt")