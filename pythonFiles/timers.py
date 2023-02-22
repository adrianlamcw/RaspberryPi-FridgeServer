import time

def set_timer(seconds):
    
    # Start the timer
    start_time = time.time()

    # Check the elapsed time
    elapsed_time = time.time() - start_time

    # Keep looping until enough seconds have passed
    while elapsed_time < seconds:
        elapsed_time = time.time() - start_time