# Lab 2

This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.



## Due

This lab is due at the end of the day that is before your next lab:
- section `NAA`: Monday, Oct 5 2026, @ 23:59
- section `NBB`: Thursday, Oct 8 2026, @ 23:59



## Objectives

- Practice performing a full analysis.
- Practice writing recursive functions.
- Understanding the difference between wall-clock time and runtime.



## Setup

Set up your repository as instructed in [lab 0](lab-00.md).  In your repository, create a folder named `lab-02` and put there the the content of the folder `release` and update those files as instructed below.

Unless otherwise stated, all writing goes into the file `lab2.md`.



## Part A: In-Class Discussion

Students who are more than 15 minutes late at the lab, cannot get credit for this part (this part will be considered incomplete for them).

This part of the lab must be done in class.  Get together into a small group 3 to 4 students.  Write your complete answers in the `lab2.md` in your repository.

The following are 3 functions that will all return the same thing given the same parameters.  They are 3 very different approaches to exactly the same problem.

This may be useful: https://wiki.python.org/moin/TimeComplexity

1. **WITHOUT DOING AN ANALYSIS** (so by gut feeling alone), rank the 3 functions based on which one is faster and producing the output. Discuss this with your group and explain why you say what you say.
2. Determine what these functions do, state it in English.  This does not mean "it has this loop, then it compares ..."; thats not what is being asked for.  State it like "this function is passed and array and a key value, it will ... and return ...".  Include an example for a given list/key, what the return value is.  To help understand what the functiond do, pick a sample input and follow the code to check how the output looks like for that input.
3. Run `lab2_timing.py` in your repo.  Does the timing validate your ranking?  Any surprises?
4. Analyze the 3 functions (this can be split amoungst your group members).  You need to do at least one each.  Share the results.
5. Run `lab2_timing.py` with increasing values of the amount of data (increase by 1000 each time).  Is there a pattern? (Note: ensure that you are using the same "machine" as you change the data size; ideally a local computer to avoid inconsistencies).  Does the timing reflect what you expect based on your analysis?  Draw a plot in Excel that shows how the execution time increases with each input size for each function.


```python
def one(mylist, key):
	total = 0
	for i in range(len(mylist)):
		for j in range(i+1,len(mylist)):
			if i != j:
				if mylist[i] + mylist[j] == key:
					total += 1
	return total



def two(mylist, key):
	total = 0
	mylist.sort()
	i = 0
	j = len(mylist)-1
	while (i < j):
		if(mylist[i] + mylist[j] < key):
			i+=1
		elif(mylist[i] + mylist[j] > key):
			j-=1
		else:
			total += 1
			i+=1
			j-=1
	return total



def three(mylist, key):
	items={}
	total = 0
	for number in mylist:
		items[number]=1
	for number in mylist:
		other = key-number
		if(other in items):
			total+=1
	return total//2
```



## Part B: Programming

- Write the following Python functions **recursively**.
- A non-recursive solution that works will not be given credit (even if it passes testing).
- Check that your solution works by running the tester `lab2_tester.py`.


### Function 1: Factorial

Write the **recursive** function to to calculate the factorial of a positive integer. This function is passed a positive integer as parameter and returns its factorial $n!$.

$$
n! = n \times (n-1) \times (n - 2) \times (n - 3) \times   \cdots   \times 3 \times 2 \times 1
$$

By definition, $0! = 1$.

```python
def factorial(n)
    # your solution here
```



### Function 2: Linear Search

Write the **recursive** function to perform linear search. This function receives a list of values and a key, searches linearly in the list for the key; if a matching key is found in the list, function returns index of where the key was found. If the key is not found, function returns `-1`.

NOTE: you are not allowed to use any of the library/built-in functions for this problem. The only function you are allowed to use is `len()` to find the size of the list.

```python
def linear_search(list, key)
    # your solution here
```

**HINT:** you may need to write the actual recursive function with a different set of arguments to accomplish this task; `linear_search` will call the recursive function.



### Function 3: Binary Search

Write the **recursive** function to perform binary search. This function receives a *sorted* list of values and a key, searches in the list using the binary search algorithm; if a matching key is found in the list, function returns index of where the key was found. If the key is not found, function returns `-1`.

NOTE: you are not allowed to use any of the library/built-in functions for this problem. The only function you are allowed to use is `len()` to find the size of the list.

```python
def binary_search(list, key)
    # your solution here
```

**HINT:** you may need to write the actual recursive function with a different set of arguments to accomplish this task; `binary_search` will call the recursive function.



## Submitting Your Lab

Push an updated version of of the files found in the `release` and any other relevant files into the `lab-02` folder of your lab repository. Submit in BlackBoard the link to your repository.



## Lab Rubric:

- For part A to be completed, you must arrive in class within 15 minutes of the start of your lab period, participate in the class discussion and all 5 of tasks/answers are added to `lab2.md`. The analysis must be complete:
  - on each line of the code, identify how many operations are performed, what are those operations, if the line is part of a loop state how many times the loop is running.
  - write your $T(n)$ by copying the number of operations from each line of code (identified above).
  - simplify your $T(n)$.
  - identify the dominant factor in the $T(n)$ formula.
  - state the complexity using *Big-O* notation.
- For part B to be completed, all three functions must be implemented in a *recursive* manner and they must pass testing with the provided tester.

| Criteria       | Poor - 0%                        | Fair - 50%                                 | Good - 100%         |
| -------------- | -------------------------------- | ------------------------------------------ | ------------------- |
| Lab Completion | All parts are incomplete/missing | (part A) or (part B) is incomplete/missing | All parts completed |
