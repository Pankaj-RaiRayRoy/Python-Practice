raw_scores = ["820", "640", "-999", "710", "640", "A+", "790", "580", "820", "-15", "710"]
cleansed_scores = []
deduplicated_list = []

#step_1 : removing all the non digit values:-
for element in raw_scores:
    if element.isdigit():
        new_element = int(element)
        cleansed_scores.append(new_element)

#deduplicating:-
for element in cleansed_scores:
    if element not in deduplicated_list:
        deduplicated_list.append(element)     

#sorting in descending:-
deduplicated_list.sort(reverse = True)

print("Final Cleansed List: ", deduplicated_list)
print("Total number of valid unique applicants: ", len(deduplicated_list))
median_index = len(deduplicated_list) // 2
print("The median score of the cleansed pool is :", deduplicated_list[median_index])




            




