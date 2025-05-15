'''module docset'''
def print_apples():
    '''various data types containing "apples".'''
    fruits_tuple = ("banana", "orange", "kiwi", "apple")
    fruits_list = ["dragon", "apple", "pear"]
    fruits_dict = {
        "least_favourite": "cherry",
        "most_favourite": "apple"
    }
    print(fruits_tuple[3])
    print(fruits_list[1])
    print(fruits_dict["most_favourite"])

print_apples()
