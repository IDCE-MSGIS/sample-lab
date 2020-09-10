# Lab 1 Assignment: Calculating Rainfall

1. Summarize what your script does or the problem you were trying to solve:

My code calculates the length and width and volume of the run-off area and measures the run-off volume of water *(in gallons)* given the rainfall amount *(in inches)* for a plot of land in Kenya.

2. Summarize any major errors you encountered and what sources they used to resolve the errors:

I came across a problem while trying to provide the results to the second decimal places. The conversion of run-off volume was in cubic inches which I tried to convert into gallons. While I used the formula to convert run-off volume in gallons **(run-off volume//231)** and **round** function to limit the result in second decimal places, it always ended in `.0` after the integer.

3. How you fixed the errors, or where the error is if you couldn't figure something out.

I used **"run-off volume 0.004329"** instead of **"run-off volume//231"** and then the second decimal places arrived in the result.
