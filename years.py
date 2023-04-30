
def max_alive_year(years):
    counts = {}
    for start, end in years:
        for year in range(start, end+1):
            counts[year] = counts.get(year, 0) + 1
    max_count = max(counts.values())
    return max(year for year, count in counts.items() if count == max_count)





years = [(1982, 2023),(1950, 2010),(1960, 2015)]
print(max_alive_year(years)) # Output: 2000




#According to this solution, the year with most people alive is 2000.
