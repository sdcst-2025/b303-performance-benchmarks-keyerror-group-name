## B403 Performance Benchmarks

In computing, we are often very concerned about performance and speed.  While calculations can be very short for small amounts of data, once you start dealing with large quantities, system performance can be *very* important.  Who wants to sit around waiting for calculations to complete or pages to load?

In this lesson, we will be seeing some of the ways that we can test the speed of an algorithm, and see how that speed scales up (mostly down!) as there is increasing amounts of data.  We will also see how worst and best case scenarios can help.

Assignment:
Come up with a proposal for a project that can test how long it will take to sort a set of data of various sizes.  We will eventually need:
* best case data
* worse case data
* random data
* different sorting algorithms
* a way to test how long it will take to sort data (performance!)
* a way to compare our results

Task 1 Generating sort data.
Write a program that will ask for the user to enter in an integer. This will represent the number of data points in each file.
Using the integer, generate 3 file that contains best case, worst case and random data.  sampleData.py sampleBest.py and sampleWorst.py show you what your file might look like with 7 data points.
Make use of a class object to create your program.