def merge(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by start time
    intervals.sort()

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        last_start, last_end = merged[-1]
        curr_start, curr_end = intervals[i]

        # If overlapping, merge
        if curr_start <= last_end:
            merged[-1][1] = max(last_end, curr_end)
        else:
            merged.append(intervals[i])

    return merged


# Example usage
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
