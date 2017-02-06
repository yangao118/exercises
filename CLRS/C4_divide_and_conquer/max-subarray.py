#!/usr/bin/env python

def find_max_subarray_brute_force(A, p, r):

    max_array_sum = A[p]
    max_left = p
    max_right = p

    for i in xrange(p,r + 1):
        array_sum = 0
        for j in xrange(i, r + 1):
            array_sum += A[j]
            if array_sum > max_array_sum:
                max_array_sum = array_sum;
                max_left = i
                max_right = j

    return (max_left, max_right, max_array_sum)

def find_max_crossing_subarray(A, low, mid, high):

    sum_left = 0
    for i in xrange(mid, low-1, -1):
        sum_left += A[i]
        if i == mid:
            max_left = i
            max_sum_left = sum_left
        if sum_left > max_sum_left:
            max_sum_left = sum_left
            max_left = i

    sum_right = 0
    for j in xrange(mid+1, high+1):
        sum_right += A[j]
        if j == mid + 1:
            max_right = j
            max_sum_right = sum_right
        if sum_right > max_sum_right:
            max_sum_right = sum_right
            max_right = j

    return (max_left, max_right, max_sum_left + max_sum_right)

def find_max_subarray_recursive(A, p, r):
    if (p == r):
        return (p, r, A[p])

    mid = (p + r) / 2

    (left_low, left_high, left_sum) = find_max_subarray_recursive(A, p, mid)
    (right_low, right_high, right_sum) = find_max_subarray_recursive(A, mid + 1, r)
    (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, p, mid, r)

    if (left_sum > right_sum) and (left_sum > cross_sum):
        return (left_low, left_high, left_sum)
    elif (right_sum > left_sum) and (right_sum > cross_sum):
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)

# Ugly but easy to comprehend

def find_max_subarray_linear(A, p, r):
    max_low = p
    max_high = p
    max_sum = A[p]
    tmp_sum = A[p]

    for i in xrange(p+1, r+1):
        if A[i] > 0:
            if max_high == i - 1:
                max_sum += A[i]
                max_high = i
                tmp_sum += A[i]
            else:
                if tmp_sum > 0:
                    tmp_sum += A[i]
                    if tmp_sum > max_sum:
                        max_high = i
                        max_sum = tmp_sum
                else:
                    max_sum = A[i]
                    max_low = max_high = i
                    tmp_sum = max_sum
        else:
            if A[i] > max_sum:
                max_sum = A[i]
                max_low = max_high = i
                tmp_sum = max_sum
            else:
                tmp_sum += A[i]

    return (max_low, max_high, max_sum)

def main():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    print A

    print "find_max_subarray_brute_force: ", find_max_subarray_brute_force(A, 0, len(A) - 1)

    print "find_max_subarray_recursive: ", find_max_subarray_recursive(A, 0, len(A) - 1)

    print "find_max_subarray_linear: ", find_max_subarray_linear(A, 0, len(A) - 1)

    B = [-2, -3, -1, -4, -120, -23, -40, -23, -8, -7]

    print B

    print "find_max_subarray_brute_force: ", find_max_subarray_brute_force(B, 0, len(B) - 1)

    print "find_max_subarray_recursive: ", find_max_subarray_recursive(B, 0, len(B) - 1)

    print "find_max_subarray_linear: ", find_max_subarray_linear(B, 0, len(B) - 1)


if __name__ == "__main__":
    main()
