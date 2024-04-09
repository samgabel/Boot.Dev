def count_names(list_of_lists: list[list], target_name: str) -> int:
    count = 0
    for list_item in list_of_lists:
        for name in list_item:
            if target_name is name:
                count += 1
    return count


# has a time complexity of O(mn)
# where m = num of lists; n = num of items/list
#-----------------------------------------------------------------------


lofl = [["sam", "bam", "tam"], ["sam", "bam", "tam"], ["sam", "bam", "tam"]]
target = "sam"

print(count_names(lofl, target))
