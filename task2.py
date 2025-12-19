import heapq

def merge_k_lists(list_of_sorted_lists):
    s_list = [element for  el_list in list_of_sorted_lists for element in el_list]
    heapq.heapify(s_list)
    return [heapq.heappop(s_list) for el in range(len(s_list))]
    



print(merge_k_lists([[1, 2, 3], [4, 5], [6]]))