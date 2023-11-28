def time_conversion(hour, minute, period):
    # Convert time from 12-hour format to 24-hour format
    if period == "am" and hour == 12:
        # Handle special case: 12 am -> 00 hours
        hour = 0
    elif period == "pm":
        if hour != 12:
            # Add 12 hours to the hour to convert from pm to 24-hour format
            hour += 12
        # If it's 12 pm (noon), it remains 12 in 24-hour format
        elif hour == 12:
            hour = 12
    
    # Format the time in 24-hour format with leading zeros
    converted_time = f"{hour:02d}{minute:02d}"
    
    # Print the original time and its converted 24-hour format
    print(f"The time {hour:02d}:{minute:02d} {period} in 24-hour format is: {converted_time}")
    
    # Return the converted time
    return converted_time

# Example usage:
hour_input = 5
minute_input = 30
period_input = "pm"

# Calling the function with the provided inputs
converted_time_result = time_conversion(hour_input, minute_input, period_input)
