#q5
def find_peaks_index(number_list):
    peaks = []
    for i in range(1, len(number_list) - 1):
        if number_list[i] > number_list[i - 1] and number_list[i] > number_list[i + 1]:
            peaks.append(i)
    return peaks

def find_mountain(number_list, peak):
    left = peak
    while left > 0 and number_list[left - 1] < number_list[left]:
        left -= 1
    right = peak
    while right < len(number_list) - 1 and number_list[right] > number_list[right + 1]:
        right += 1
    return number_list[left:right + 1]

def largest_mountain(number_list):
    peaks_index = find_peaks_index(number_list)
    largest_mountain = None
    for peak in peaks_index:
        mountain = find_mountain(number_list, peak)
        if largest_mountain is None or len(mountain) > len(largest_mountain):
            largest_mountain = mountain

    return largest_mountain if largest_mountain else "No mountain found"


inp_list = input("input: ").split(",")
inp_list = [int(num) for num in inp_list]
print(largest_mountain(inp_list))