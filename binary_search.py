nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
search = int(input("Enter a number to search: "))

low = 0
high = len(nums) - 1

while low <= high:
    mid =(low + high) // 2
    print(mid)
    if nums[mid] == search or nums[low]== search or nums[high]== search:
        if nums[mid] == search:
            print(f"Number {search} found at index nums[{mid}]")
        elif nums[low] == search:
            print(f"Number {search} found at index nums[{low}]")
        elif nums[high] == search:
            print(f"Number {search} found at index nums[{high}]")
        break
    elif search < nums[mid]:
        high = mid - 1
       
    elif search > nums[mid]:
        low = mid + 1
        

