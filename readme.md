# Task 1 - Hacking 101
## Optional challange
### Problem
> It’s possible that the list of valid letters and phrases for hacks isn’t complete. Can you describe how you would change your algorithm so it could calculate hack power for dynamically provided letters and phrases (e.g.: “hack_calculator(hack=’advantage’, letters={'a': 1 , 'd': 2, 'e': 5, 'g': 2, 'n': 1 , 't': 4, 'v': 7}, phrases={‘ad’: 1 0, ‘ant’: 1 3, ‘age’: 24, ‘van’: 1 3, ‘tag’: 5}”)?
### Solution
The generalized version of the problem requires designing a new method to find the largest total contribution from special phrases. Let's call that value LTE for short.
We can use dynamic programming to solve the new task. Proposed procedure works in a bottom-up manner it is a deriviation of the ["Matrix chain multiplication"](https://en.wikipedia.org/wiki/Matrix_chain_multiplication) algorithm.  It calulates LTE for all subhacks (substrings of the hack) of length 2, then for subhacks of length 3 etc. Ultimately we receive LTE of entire hack. In the following pseudocode I denote a substring of the hack by hack[m,n].

* Let d[i,j] represents LTE of hack[i,j] for 1 <= i <= j <= n. d[i, j] is the optimal solution
for subhacks hack[i,j]
* d[i,i]= 0 since a single letter can not be a special phrase
* Let phrases[m] contains a list of all special phrases of length m
Thus the optimal solution for the string hack[i,j] must break at a point k for i <= k <= j. There are two possibilites:
* length(hack[i,j]) == m and length(phrases[m]) != 0. Then there may exist a special phrase of length m that overlaps between hack[i,k] and hack[k,j] and has larger power contribution than any shorter phrases that were matched to the subhacks. 
* If there is no such a phrase then d[i,j] = d[i,k] + d[k+1,j]. 

