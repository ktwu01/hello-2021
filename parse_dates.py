#!/usr/bin/env python3
import re
from datetime import datetime

def parse_dates_from_file(filename):
    """Extract all dates from the markdown file"""
    dates = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all YYYY-MM-DD patterns
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    matches = re.findall(date_pattern, content)
    
    # Convert to datetime objects and sort
    for date_str in matches:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            dates.append(date_obj)
        except ValueError:
            print(f"Invalid date format: {date_str}")
    
    # Remove duplicates and sort
    unique_dates = sorted(list(set(dates)))
    
    return unique_dates

if __name__ == "__main__":
    dates = parse_dates_from_file("hello-2021/hello-2021.md")
    
    print(f"Found {len(dates)} unique dates:")
    print(f"Date range: {dates[0].strftime('%Y-%m-%d')} to {dates[-1].strftime('%Y-%m-%d')}")
    
    # Print first 10 and last 10 dates
    print("\nFirst 10 dates:")
    for date in dates[:10]:
        print(f"  {date.strftime('%Y-%m-%d')}")
    
    print("\nLast 10 dates:")
    for date in dates[-10:]:
        print(f"  {date.strftime('%Y-%m-%d')}")
    
    # Save dates to a file for the next step
    with open("dates_to_commit.txt", "w") as f:
        for date in dates:
            f.write(f"{date.strftime('%Y-%m-%d')}\n")
    
    print(f"\nSaved {len(dates)} dates to dates_to_commit.txt") 