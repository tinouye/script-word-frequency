def prompt_queries():
    print("\n\n")
    print("Enter keywords you'd like to search for separated by a comma")
    print("Enter '1' to use the default search ('darkness', 'heart')")
    return_keyword = input("Please enter a search query ('qq' to quit): ")
    return return_keyword

def parse_input(user_input):
    if user_input == "1":
        return ["darkness", "heart"]
    else:
        split_input = user_input.split(",")
        return [i.strip() for i in split_input]


def find_number_of_instances_in_string(query, body):
    match_index = 0
    num_found = 0

    while match_index != -1:
        # string.find returns the index of the first found instance
        # Move up the starting index to after the found word every time an instance is found
        while match_index != -1:
            match_index = body.find(query, match_index)
            if match_index != -1:
                num_found += 1
                match_index += 1
    
    return num_found

def search_script(keyword_arr): 
    lines_including_keyword = []
    # Initialize dictionary with key/value keyword/count found
    keyword_count = {}
    for word in keyword_arr:
        keyword_count[word] = 0

    with open("khScript.txt") as f:
        # Iterate through each line of the script
        for line in f:
            # Iterate through each keyword query
            for word in keyword_arr:
                num_found = find_number_of_instances_in_string(query=word.lower(), body=line.lower())
                keyword_count[word] += num_found
                if num_found > 0:
                    lines_including_keyword.append(line)
    
    return keyword_count, lines_including_keyword

def output_lines(lines):
    for line in lines:
        print(line)

def output_dict(dict):
    for key in dict:
        val = dict[key]

        # Add the s in times for plural
        if val == 1:
            s = ""
        else:
            s = "s"
        
        print(f"'{key}': {val} time{s}")

def main(user_input_mode):
    user_input = ""

    while user_input != "qq":
        user_input = prompt_queries()
        if user_input == "qq":
            break

        keyword_arr = parse_input(user_input)
    
        keyword_count, lines_including_keyword = search_script(keyword_arr)

        output_lines(lines_including_keyword)
        output_dict(keyword_count)

main(user_input_mode=False)