from memory_profiler import profile


fp = open('memory_profile.log', 'w+')


@profile(stream=fp)
def func_to_profile():
    a = [1] * 100000


func_to_profile()
