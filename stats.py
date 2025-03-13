def get_num_words(filepath):
    count_file = ""
    with open(filepath) as f:
        count_file = f.read()
    list_words = count_file.split()
    counter = 0
    for words in list_words:
        counter += 1
    return counter

def get_num_characters(file_text):
    char_counts = {}
    for F in file_text:
        f_lower = F.lower()
        if f_lower in char_counts:
            char_counts[f_lower] += 1
        else:
            char_counts[f_lower] = 1
    
    return char_counts



def get_sorted_characters(dict_sort):
    
    result = [{"char": k, "count": v} for k, v in dict_sort.items()]
    result.sort(reverse=True, key=lambda x: x["count"])
    return result

   
    