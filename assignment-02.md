# CMPS 2200 Assignment 2

**Name:**_____Sean Hall____________________

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  
.  
.  
.  
.  
  * $W(n)=5W(n/4)+n$
.  
.  
.  
.  
.  
  * $W(n)=7W(n/7)+n$
.  
.  
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  
.  
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  
.  
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.  
.  
.  
.  
  * $W(n)=W(n-1)+2$
.  
.  
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
.  The depth here is n
  work lvl 0: n^c
  work lvl 1: (n-1)^c
  work lvl 2: (n-2)^c. 
  While the work at each level decreases, it does not decrease geometrically and thus each level's work can be treated as n^c. Thus the total work is n^c * n. Thus, O(n^(c+1))
.  
.  
.  
  * $W(n)=W(\sqrt{n})+1$
    Becauses the input is decreases by a square root, not every input results in a nice base case. Most result in a floating number. The tree depth is n^(1/2k). When we want the final node to 1, we have to set n^(1/2k) = 1. We can take the log_base_n of each side to get 1/2k = 0 (because log base anything of 1 equals 0). However, this is only true as k = infinity. Thus our base case will be different for each input. So we can assume O(loglogn).

2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


