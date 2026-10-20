## Part A: Analysis

### Function 1

```python
def function1(value, n):
	if (n == 0):
		return 1
	elif (n == 1):
		return value
	else:
		return value * function1(value, n - 1)
```
Base case: n = 0

```python
if (n == 0):                          # 1 ("==")
    return 1                          # 1 ("return")
elif (n == 1):                        # 0 (skipped)
    return value                      # 0 (skipped)
else:                                 # 0 (skipped)
    return value * function1(value, n - 1)     # 0 (skipped)
```

T(n) = 2

Base case: n = 1

```python
if (n == 0):                          # 1 ("==")
    return 1                          # 0 (skipped)
elif (n == 1):                        # 1 ("==")
    return value                      # 1 ("return")
else:                                 # 0 (skipped)
    return value * function1(value, n - 1)     # 0 (skipped)
```
  T(n) = 1 + 1 + 1  = 3

Recursive case: n > 1

```python
if (n == 0):                          # 1 ("==")
    return 1                          # 0 (skipped)
elif (n == 1):                        # 1 ("==")
    return value                      # 0 (skipped)
else:                                 # 0 (skipped)
    return value * function1(value, n - 1) # 3 ("return", "*", "-") + T(n - 1)
```

T(n) = 1 + 1 + 3 + T(n - 1) 

= T(n - 1) + 5 

= T(n-2) + 5 + 5 

= T(n-3) + 5 + 5 + 5

=> T(n) = T(n-k) + k x 5

To reach base case T(1): n - k = 1

k = n - 1

Substitute k = n - 1:

T(n) = T(1) + 5(n - 1)

= 3 + 5n - 5

= 5n - 2

DF: 5n
Complexity: O(n)

### Function 2

```python
def recursive_function2(mystring, a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring, a + 1, b - 1)

def function2(mystring):
	return recursive_function2(mystring, 0, len(mystring) - 1)
```

Evaluating the function2:

```python
def function2(mystring):
    return recursive_function2(mystring, 0, len(mystring) - 1) 3 + T_rec ()

```

$$
T_{func2}(n) = T_{rec}(n - 1) + 3
$$

### Function 3

```python
def function3(value, n):
	if (n == 0):
		return 1
	elif (n == 1):
		return value
	else:
		half = n // 2
		result = function3(value, half)
		if (n % 2 == 0):
			return result * result
		else:
			return value * result * result
```



## Part C: Reflection

Answer the following questions:
1. Describe how to approach writing recursive functions, what steps do you take?
2. Describe the process of analyzing recursive functions.  How does it differ from analyzing non-recursive functions?  How is it the same? 
3. Described what you learned in the implementation for the linked lists.  What approach did you take?  What bugs did you find most difficult to fix.
