# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are ordered, iterable sequences of data, and these data may be a mixture of types (integers, floats, strings, variables, etc.). Both can be printed, sliced, concatenated, or multiplied, resulting in a new object of the respective data type. Tuples are immutable; only lists may be altered. As such, any methods such as .pop(), .insert(), .append(), or .sort() that alter the contents of a list cannot be used on a tuple. Only tuples can be used as dictionary keys.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are iterable sequences of data, and the data may be a mixture of types for each, as with tuples. Sets are unordered and thus do not support indexing, and also do not include duplicates, whereas both of these are supported with lists. To find the actual location of an element, one can only use a list, given the lack of indexing with a set. Though were one trying only to discern membership of an element in a list, it would probably be easier to use a set if the list were substantially large and included many duplicates, e.g.:  
```python
reallyBigListSet = set(reallyBigList)
foo in reallyBigListSet
```
> > Examples of use:  
```python
# how many occurrences of each test score?
scoreList = [70, 85, 80, 95, 85, 90, 80, 100, 95, 85, 75]
scoreSet = set(scoreList)
for score in scoreSet:
    print(f"{score}:", scoreList.count(score))
# or to make sure scores were presented in asecending order
scoresAsc = sorted(scoreSet)
for score in scoresAsc:
    print(f"{score}:", scoreList.count(score))
```

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





