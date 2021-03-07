"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    greatest = max(incoming_list)
    return greatest


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    least = min(incoming_list)
    return least


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    try:
        total = sum(incoming_list)
    except:
        total = 0
    return total


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    greatest = 0
    longest_key = ""
    try:
        if len(incoming_dict > 0):
            for k in incoming_dict:
                value = incoming_dict.get(k)
                if len(value) > greatest:
                    longest_value = value
                    greatest = len(value)
                    longest_key = k
                    return longest_key
        else:
            return None
    except:
        return None
