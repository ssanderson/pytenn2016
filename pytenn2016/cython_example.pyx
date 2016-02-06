cpdef cyfact(int n):
    cdef int acc = 1
    cdef int i
    for i in range(1, n + 1):
        acc *= i
    return acc
