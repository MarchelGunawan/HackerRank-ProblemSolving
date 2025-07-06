# Time Convertion
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
- $$ s = "12:01:00PM" $$
Return '12:01:00'

- $$ s = "12:01:00AM" $$

Return '00:01:00'.

# Solution
The solution using technic called [slicing](https://www.w3schools.com/python/python_strings_slicing.asp), by that technic we can take specific character from string.

First we need to take AM or PM from the string by using code below:

```python
diff = time[8:10]
```

after that we need to take hour, min and sec in the string. Since the changes will affected to the hour so after we slicing the hour we need change it into integer. Since the min and sec doesn't affected so we can slice min and sec in one variable.

Why we need to do that? because if time shown PM so later the hour just need to add 12, for example 01:00 PM mean 13:00 which mean 1 + 12.

But for the AM will be special case because the changes when in AM just for 12:00 AM to 00:00 and when 01:00 AM to 01:00 which mean the changes just affected to 12:00 AM.

After that if the hour less then 10 we need to add 0 in front of the changes hour. Because the format is double digit.
```python
def timeConvertion(time: str):
    # To take either AM or PM
    diff = time[8:10]
    """
        Need to take 2 digit of hour from time
        and convert it into integer.
        So later we can add 12 if it's PM 
        and substract it if it's AM 
    """
    hour = int(time[:2])
    minandsec = time[2:8]
    if diff == "PM":
        hour += 12
        """
            For the AM it will be a special case when hour is 12 since 12AM means 00 and 1 AM mean 01
            so we need substract if the hour is 12.
        """
    elif diff == "AM" and hour == 12:
        hour -= 12
    # we need to changeback the hour from integer to string.
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    return hour+minandsec

```
