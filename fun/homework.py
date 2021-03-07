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
    total = 0
    for x in range(0, len(incoming_list)):
        total = total + incoming_list[x]
    return total


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    longest = len(max(incoming_dict))
    return longest
