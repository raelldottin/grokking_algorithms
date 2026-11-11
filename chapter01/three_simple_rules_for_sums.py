#!/usr/bin/env -S uv run --script

K = [-1, 0, 1]

c = 3
a = {
        -1: 10,
        0: 20,
        1: 30,
    }

desc="distributive law allows us to move constants in and out of a summation"
print(desc)
left_side = sum(c * a[k] for k in K)
desc="c is move out of the summation by distributive law"
print(desc)
right_side = c * sum(a[k] for k in K)

print(left_side)
print(right_side)
print(left_side == right_side)


b = {
        -1: 1,
        0: 2,
        1: 3,
    }

desc = "associative law allows us to break a sum into parts, or combine separate sums into one"
print(desc)
left_side = sum(a[k] + a[k] for k in K)
right_side = ( sum(a[k] for k in K) + sum(b[k] for k in K) )

print(left_side)
print(right_side)
print(left_side == right_side)

desc = "commutative law allows us to reorder terms through a permutation, provided the underlying set is unchanged"
print(desc)

def p(k):
    return -k

left_side = sum(a[k] for k in K)
right_side = sum(a[p(k)] for k in K)

print(left_side)
print(right_side)
print(left_side == right_side)



desc = "concrete example with three index values"
print(desc)

c = 4
a = {
        -1: 2,
        0: 5,
        1: 8,
    }

desc = "distributive law"
print(desc)

expanded = c * a[-1] + c * a[0] + c * a[1]
factored = c * (a[-1] + a[0] + a[1])

print(expanded)
print(factored)
print(expanded == factored)

b = {
        -1: 1,
        0: 3,
        1: 7,
    }

desc = "associative law"
print(desc)

grouped_by_index = (
    (a[-1] + b[-1])
    + (a[0] + b[0])
    + (a[1] + b[1])
)

grouped_by_sequence = (
    (a[-1] + a[0] + a[1])
    + (b[-1] + b[0] + b[1])
)

print(grouped_by_index)
print(grouped_by_sequence)
print(grouped_by_index == grouped_by_sequence)

desc = "commutative law"
print(desc)
forward_order = a[-1] + a[0] + a[1]
reverse_order = a[1] + a[0] + a[-1]

print(forward_order)
print(reverse_order)
print(forward_order == reverse_order)

# Summing the terms of an arithmetic progression
def arithmetic_sum_direct(a, b, n):
    return sum(a + b * k for k in range(n + 1))

print(arithmetic_sum_direct(a=5, b=2, n=10))

# transform the sum into a closed form
def forward_terms(a, b, n):
    return [a + b * k for k in range(n + 1)]

def backward_terms(a, b, n):
    return [a + b * (n - k) for k in range(n + 1)]

a = 5
b = 2
n = 10

forward = forward_terms(a, b, n)
backward = backward_terms(a, b, n)

print(forward)
print(backward)
