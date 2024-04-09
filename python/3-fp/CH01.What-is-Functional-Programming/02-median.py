# calculate median without...
### any loops
### mutating any variables (setting variables is ok)

def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None

    sorted_font_sizes = sorted(font_sizes)
    median_index = len(font_sizes) // 2

    if len(font_sizes) % 2 == 0:
        return ( sorted_font_sizes[median_index] + sorted_font_sizes[median_index - 1] ) / 2
    return sorted_font_sizes[median_index]

#---------------------------------------------------------------------------------------------------

list_1 = [10, 12, 14]
list_2 = [9, 11, 16, 20]

#------------------------------------------------

print("---------------------------------")
print(f"Input: {list_1}")
print(f"Expected: 12")
print(f"Actual: {get_median_font_size(list_1)}")
if get_median_font_size(list_1) == 12:
    print("Pass")
else:
    print("Fail")

print("---------------------------------")
print(f"Input: {list_2}")
print(f"Expected: 13.5")
print(f"Actual: {get_median_font_size(list_2)}")
if get_median_font_size(list_2) == 13.5:
    print("Pass")
else:
    print("Fail")
