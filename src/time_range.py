def get_range(start_times, end_times):

    if not isinstance(start_times, list):
        return "Input lists only"
    if not isinstance(end_times, list):
        return "Input lists only"

    start_len = len(start_times)
    end_len = len(end_times)

    if start_len != end_len:
        return "Input lists are not the same length"

    if start_len < 2:
        return "Minimum 2 inputs needed"
    
    times = start_times + end_times
    check_intfloat = all(isinstance(x, (int, float)) for x in times)
    if not check_intfloat:
        return "Input float/int data only"
    
    mi = max(start_times)
    ma = min(end_times)

    if mi >= ma:
        return "No overlap" 

    return [mi, ma]