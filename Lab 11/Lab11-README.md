# Lab 10  
Rae Sheng  
PHYS 1200  
Professor Zahra Alavi  
11 May 2025  
  
## **Final 1:** Brownian Motion  
**Objective:** In this lab, you'll use Python to generate two-dimensional random walks, plot their trajectories, and look at the distribution of end points for a large number of random walkers.  
           
**Sections:**
  * 1.1 - Generating and plotting trajectories  
      * Make a random walk trajectory, and then plot it. To remove any distortion, use the command plt. axis ('square') or plt.axis ('equal') after making the plot.  
      * Now make four such trajectories, and look at all four side by side. Use plt.figure() to create a new figure window. You can access the individual subplots by using commands like plt.subplot (2, 2, 1) before the first pIt.plot command, plt.subplot (2, 2, 2) before the second plt.plot command, and so on. Python may give each plot a diﬀerent magnification. Consult help(plt.xlim) and help(pIt.axis) to find out how to give each of your plots the same x and y limits.  

  * 1.2 - Plotting the displacement distribution  
      * Once you have a code that works, increase the number of random walks from 100 to 1000. Make a scatter plot of the end points.  
      * Use plt.hist to make a histogram of the displacement values.  
      * Make a histogram of the quantity displacement**2.  
      * Your result from C may inspire a guess as to the mathematical form of the histogram. Use semilog and log-log axes to test for exponential or power law relationships.  
      * Use np.mean to find the average value of displacement**2 (the mean-square displacement) for a random walk of 1000 steps.  
      * Find the mean-square displacement of a 4000-step walk. If you wish to carry the analysis further, see if you can determine how the mean-square displacement depends on the number of steps in a random walk.  

**Final 2:** Rare Events
  * To be added!
