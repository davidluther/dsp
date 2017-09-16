[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

---

**Exercise summary:** Height distribution for adults is relatively normal, with µ = 178 cm / σ = 7.7 cm for men and µ = 163 cm / σ = 7.3 cm for women. To join the Blue Man group, one must be a male beween 5'10" and 6'1". What percentage of the US male population satisfies this condition?

---

34.27% of the US male population falls within this range.

#### Code used to solve exercise:
```python
# pre-filled code that imports normal distrib model
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

# convert heights to cm
def imp_to_std(ft, inches):
    inches += (ft * 12)
    return round(inches * 2.54, 2)

h1 = imp_to_std(5,10)
h2 = imp_to_std(6,1)

# find normal values for each height
ph1 = dist.cdf(h1)
ph2 = dist.cdf(h2)

# and subtract first from second to get percent of males in range
p_slice = round((ph2 - ph1) * 100, 2)
print(f"Percentage of males between 5'10\" and 6'1\": {p_slice}%")
```
