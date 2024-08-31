# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.


import time
time_for_next_retry = 1
retries = 0
while retries <= 5:
    print( "this is" , retries , "th retry  and time for next retry  is ", time_for_next_retry , "seconds")
    retries += 1
    time.sleep(time_for_next_retry)
    time_for_next_retry*=2

print("Reached max retries")

 