import time

def dummy_loop(num_of_iterations):
    dummy_variable = 0
    for i in range(0, num_of_iterations):
        dummy_variable += 1
    return dummy_variable

    '''
    increase number of iterations and time stamp for every 1 million
    1,000,000 to 10,000,000 in 1,000,000 jumps
    output

    '''


def test_scalability():
    prev_time = time.time()
    count = 0
    time_taken = 0
    loop_diff = 1000000
    print "================================================================\n"
    print "\tNumber of Loop\t\tTime taken in Sec\n"
    for i in range(1,11):
        count =  dummy_loop(i * loop_diff)
        current_time = time.time()
        time_taken = (current_time - prev_time)
        prev_time = current_time

        print "\t\t%s \t\t%s \n" %(count, time_taken)
    print "================================================================\n"

test_scalability()

