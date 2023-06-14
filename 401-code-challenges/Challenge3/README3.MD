# Challenge-3

Created a function that took in an array and a key & searched for key within the array. Returned index of located key within the array or a -1 in the case of the key not existing within the array.

## Whiteboard Process

![Insert Shift Array](/401-code-challenges/images/challenge3.png)

## Approach & Efficiency

- Created function to take list and a value as an input.
- established first, last & middle index of list.
- Started loop to search for value.
- If value is not found -1 is returned.
- If middle index matches value the output is the value and its position
- If the middle index is greater than the target element the first 1/2 of list searched
- If the middle index is less than the target element the last 1/2 of list searched
- The loop continues in this fashion until narrowed down index position
- If value is not found -1 is returned.

## Solution:

def binary_search(list_num , to_search):

    first_index = 0

    size = len(list_num)

    last_index = size - 1

    mid_index = (first_index + last_index) // 2

    # print(mid_index)

    mid_element = list_num[mid_index]

    # print(mid_element)



    is_found = True

    while is_found:

        if first_index == last_index:

            if mid_element != to_search:

                is_found = False

                return " -1"



        elif mid_element == to_search:

            return f"{mid_element} occurs in position {mid_index}"



        elif mid_element > to_search:

            new_position = mid_index - 1

            last_index = new_position

            mid_index = (first_index + last_index) // 2

            mid_element = list_num[mid_index]

            if mid_element == to_search:

                return f"{mid_element} occurs in position {mid_index}"



        elif mid_element < to_search:

            new_position = mid_index + 1

            first_index = new_position

            last_index = size - 1

            mid_index = (first_index + last_index) // 2

            mid_element = list_num[mid_index]

            if mid_element == to_search:

                return f"{mid_element} occurs in position {mid_index}"







list_container = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]

print(binary_search(list_container , 81))

print(binary_search(list_container , 10))



## Contributers:

Logan Reese

## Dependencies:

Free Code Camp, Replit
