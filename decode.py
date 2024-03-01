def decode(message_file):
    with open("coding_qual_input.txt", "r") as file:
        lines = file.readlines()
        separated_lines = sorted(lines, key=lambda string:int(string.split()[0]))
        refined_separated_lines = [item.strip() for item in separated_lines]
        
        separated_lines_object = {}
        for item in refined_separated_lines: 
            key, value = item.split()
            separated_lines_object[int(key)] = value
        prestart = None
        step = 1
        start_point = 1
        end_point = len(separated_lines_object)
        # keys_to_select = range(start_point, end_point + 1, step)
        keys = separated_lines_object.keys()
        # print(keys)
        for key in keys:
            if prestart is not None:
                
        # result = ' '.join(separated_lines_object[key] for key in keys_to_select)
        # print(result)


decode("coding_qual_input.txt")