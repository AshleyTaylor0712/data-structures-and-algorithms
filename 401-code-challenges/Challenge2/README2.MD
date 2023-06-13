# Challenge-2

Created a function that takes a value and adds it into the middle of an array.

## Whiteboard Process

![Insert Shift Array](/images/challenge2.png)

## Approach & Efficiency

- Created function to take list and a value as an input.
- Used midpoint to define middle list.
- Added a value to middle list.
- Modified list is returned.

## Solution:

``` def insertShiftArray (lst, value) ```

``` midpoint = len(lst)//2 ```

```lst = lst[:midpoint] + [value] + lst[midpoint:]```

``` return lst ```

``` lst = [1, 2, 3, 4, 7, 8 ] ```

```value =10```

``` result = insertShiftArray(lst, value) ```

``` print (result) ```

``` # Output [1, 2, 3, 10, 4, 7, 8] ```

## Contributers:

Dan Quinn, Jared Ciccarello, Sarah Glass

## Dependencies:

Stack Overflow
