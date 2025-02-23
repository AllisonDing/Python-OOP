# A Python program that find the time x minutes before and after the input time

def main():
    # print the program title
    print("Find the time x minutes before and after the input time")
    time_string = input("Enter a time (hh:mm): ")
    time_shift = int(input("Enter a time shift in mins: "))   
    
    #breaks the string into a list and retrieve the hours and minutes
    time_list = time_string.split(":") 
    hours = int(time_list[0])
    mins = int(time_list[1])
    
    # convert the time into minutes
    total_mins = hours * 60 + mins

    # convert the time shift to within 24 hours (1440 minutes)
    time_shift = time_shift % 1440
    
    # find the before time
    if total_mins < time_shift:
        total_mins_before = 1440 - (time_shift - total_mins)
    else:
        total_mins_before = total_mins - time_shift
    hours_before = total_mins_before // 60
    mins_before = total_mins_before % 60
    
    # find the after time
    total_mins_after = (total_mins + time_shift) % 1440
    hours_after = total_mins_after // 60
    mins_after = total_mins_after % 60
    
    # print the results
    print("Before: {:02d}:{:02d}".format(hours_before, mins_before))
    print("After: {:02d}:{:02d}".format(hours_after, mins_after)) 

if __name__ == "__main__":
    main()