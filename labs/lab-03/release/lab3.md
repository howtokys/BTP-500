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

#### Evaluating `function2`

```python
def function2(mystring):
    return recursive_function2(mystring, 0, len(mystring) - 1) # 3 ("return", "len", "-") + T_rec(n)
```

`T_func2(n) = T_rec(n) + 3`

#### Base case: `a >= b`

```python
if (a >= b):                              # 1 (">=")
    return True                           # 1 ("return")
else:                                     # 0 (skipped)
    if (mystring[a] != mystring[b]):      # 0 (skipped)
        return False                      # 0 (skipped)
    else:                                 # 0 (skipped)
        return recursive_function2(mystring, a + 1, b - 1) # 0 (skipped)
```

`T_rec = 2`

#### Base case: `mystring[a] != mystring[b]`

```python
if (a >= b):                              # 1 (">=")
    return True                           # 0 (skipped)
else:                                     # 0 (skipped)
    if (mystring[a] != mystring[b]):      # 1 ("!=")
        return False                      # 1 ("return")
    else:                                 # 0 (skipped)
        return recursive_function2(mystring, a + 1, b - 1) # 0 (skipped)
```

`T_rec = 1 + 1 + 1 = 3`

#### Recursive case: `a < b` and `mystring[a] == mystring[b]`

```python
if (a >= b):                              # 1 (">=")
    return True                           # 0 (skipped)
else:                                     # 0 (skipped)
    if (mystring[a] != mystring[b]):      # 1 ("!=")
        return False                      # 0 (skipped)
    else:                                 # 0 (skipped)
        return recursive_function2(mystring, a + 1, b - 1)
        # 3 ("return", "+", "-") + T_rec(n - 2)
```

Each recursive call compares two characters and moves inward from both ends. Therefore, the number of characters remaining to check decreases by two each time.

`T_rec(n) = 1 + 1 + 3 + T_rec(n - 2)`

`T_rec(n) = T_rec(n - 2) + 5`

`= T_rec(n - 4) + 5 + 5`

`= T_rec(n - 6) + 5 + 5 + 5`

Therefore:

`T_rec(n) = T_rec(n - 2k) + 5k`

To reach a base case, approximately:

`n - 2k = 1`

`k = (n - 1) / 2`

Using the base-case cost `T_rec(1) = 2` for this simplified calculation:

`T_rec(n) = T_rec(1) + 5(n - 1) / 2`

`= 2 + (5n - 5) / 2`

`= (5n - 1) / 2`

**DF:** `5n`

**Complexity:** `O(n)`

The exact operation count can vary because the function may return `False` early if it finds a mismatch. If all compared characters match, it continues until the middle of the string. Since each recursive call moves inward by two positions, the number of calls grows linearly with the string length.

Including the wrapper function's constant work:

`T_func2(n) = T_rec(n) + 3`

The constant `3` does not change the overall time complexity, so `function2` is also **`O(n)`**.

---

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
