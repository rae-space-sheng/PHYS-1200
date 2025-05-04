# Lab 10  
Rae Sheng  
PHYS 1200  
Professor Zahra Alavi  
11 May 2025  
  
**Final 1:** Brownian Motion  
**Objective:** In this lab, you'll use Python to generate two-dimensional random walks, plot their trajectories, and look at the distribution of end points for a large number of random walkers.  
           
**Sections:**
  * 1.1 - Generating and plotting trajectories  
      * A. Make a random walk trajectory, and then plot it. To remove any distortion, use the command plt. axis ('square') or plt.axis ('equal') after making the plot.  
      * B. Now make four such trajectories, and look at all four side by side. Use plt.figure() to create a new figure window. You can access the individual subplots by using commands like plt.subplot (2, 2, 1) before the first pIt.plot command, plt.subplot (2, 2, 2) before the second plt.plot command, and so on. Python may give each plot a diﬀerent magnification. Consult help(plt.xlim) and help(pIt.axis) to find out how to give each of your plots the same x and y limits.  

  * 1.2 - Plotting the displacement distribution  
      * A. Once you have a code that works, increase the number of random walks from 100 to 1000. Make a scatter plot of the end points.  
      * B. Use plt.hist to make a histogram of the displacement values.  
      * C. Make a histogram of the quantity displacement**2.  
      * D. Your result from C may inspire a guess as to the mathematical form of the histogram. Use semilog and log-log axes to test for exponential or power law relationships.  
      * E. Use np.mean to find the average value of displacement**2 (the mean-square displacement) for a random walk of 1000 steps.  
      * F. Find the mean-square displacement of a 4000-step walk. If you wish to carry the analysis further, see if you can determine how the mean-square displacement depends on the number of steps in a random walk.  

**Final 2:** Rare Events  
**Objective:** In this lab, you'll use Python to visualize and plot Poisson distribution using the example of a coin that unfairly lands on tails more often.  
  
**Sections:**  
  * 2.1 - Generating and plotting trajectories  
      * A. Before you start flipping coins, plot this function for some interesting range of l values. You may find the following helpful:  
          * The factorial function can be imported from scipy.special.  
          * You need not take l ρ(l) all the way out to infinity. You'll see that quickly gets negligibly small.  
          * In Python, the elements of a vector are always numbered 0, 1, 2, 3, ..., and l is also an integer starting from zero, so l is a good array index.  
          * The value of 8^l can get very large- larger than the largest integer NumPy can store. (By default NumPy uses 64-bit integers, so the largest number it can store is 2^63 − 1.) To avoid numerical over flow - and erroneous results - use an array of floats instead of integers. Consult help(np.arange), and read about the dtype keyword argument.  
      * B. Perform N coin flip trials, each consisting of 100 flips of a coin that lands heads only 8% of the time. (Good practice: Eventually you may want to take N to be a huge number. While developing your code, make it not so huge, say, N = 1000, so that your code will run fast.)  
      * C. Get Python to count the number of heads, M, for each trial. Then, use plt.hist to create a histogram of the frequency of getting M heads in N trials. If you don't like what you see, consult help(plt. hist). (For example, plt.hist may make a poor choice about how to bin the data.)  
      * D. Make a graph of the Poisson distribution (Equation 11.2 above) multiplied by N. What's the most probable outcome? Graph this plot on the same axes as the histogram in C.  
      * E. Repeat (B-D) for N = 1000,000, and comment. This may take a while.  
  
  * 2.2 - Plotting the displacement distribution  
      * A. Construct a random string of 1's and 0's representing 1000 flips of the unfair coin. Then, plot the frequencies of waiting times of length 0, 1, 2, ..., as outlined above. Also make semilog and log-log plots of these frequencies. Is this distribution a familiar-looking function?  
      * B. What is the average waiting time between heads?  
      * C. Repeat A and B for 1000,000 flips of the coin.