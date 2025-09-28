def merge_list_to_dict(list_one, list_two):
    zipped_seq = zip(list_one, list_two)
    return dict(zipped_seq)


res_one = merge_list_to_dict(['a', 'b', 'c'], [10, True, []])
print(res_one)
    