#this function removes duplicates of the same values of the same types
def clean_list(list_to_clean):
    for i in range(len(list_to_clean) - 1):
        for j in range(i + 1, len(list_to_clean)):
            if list_to_clean[i] == list_to_clean[j] and isinstance(list_to_clean[i], type(list_to_clean[j])):
                list_to_clean[j] = None
    list_new = [i for i in list_to_clean if i != None]
    return list_new
#example:
print(clean_list([1, 1.0, '1', 2, 2.0, '2', 3, 3.0, '3', 1, 2, 3, 1.0, 2.0, 3.0, '1, 2, 3', 1.0, 2, '3'])) #[1, 1.0, '1', 2, 2.0, '2', 3, 3.0, '3', '1, 2, 3']