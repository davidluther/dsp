[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The mean weight of first babies is 7.20 lbs, and the mean weight of the others is 7.33 lbs, so first-born babies are statistically lighter than all the others, by an average of 0.15 lbs. Cohens d for the two groups is 0.089 standard deviations. Though this is roughly three times that for pregnancy lengths (0.029), it is still fairly small, not even 10% of one standard deviation.  

>> Code used to solve (using prior imports and variables in the chap02ex.ipynb file):
```python
# variables from each series
mean_f = firsts.totalwgt_lb.mean()
mean_o = others.totalwgt_lb.mean()
var_f = firsts.totalwgt_lb.var()
var_o = others.totalwgt_lb.var()
n_f = len(firsts.totalwgt_lb)
n_o = len(others.totalwgt_lb)

# calculations
mean_diff = mean_o - mean_f
sd_pooled = np.sqrt((n_f * var_f + n_o * var_o) / (n_f + n_o))
d = mean_diff / sd_pooled

print("Mean, firsts:", mean_f)
print("SD, firsts:", np.sqrt(var_f))
print("Mean, others:", mean_o)
print("SD, others:", np.sqrt(var_o))
print("Cohen's d:", d)
```
