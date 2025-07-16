Materials and instructions for BMES ML Practice.

## Git Stuff

To begin, clone this repository using `git clone`. When cloning, I recommend using an SSH url, which saves you the effort of having to type your username and password a lot. It is a bit of work to set up, but you only have to do it once per device, so I recommend doing so. Check out <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">this</a> guide for help.

Create a new file in the repository, on your local device. Make sure to include your name in the filename. After creating the file, code your project in this file. Alternatively, you can move a file from another directory to the repository (using `mv`), and then rename it. Make sure to ad your file to the staging area using `git add`.

Make sure to use `git commit` regularly to ensure that Git saves your progress, allowing you to revert to an earlier version if you mess something up. Use `git push` to add your changes to the project to the remote repository (the one on GitHub). I recommend using `git push` at least once a day, so that others can see what you're doing!

If you want to get the changes to the remote repository on your local repository (like seeing other people's projects), you can use `git fetch` to do so. I recommend doing this at least once to see how it works and get used to it. You can always check GitHub too.

The reason that we're doing all this is to familiarize ourselves with Git. Git is very useful for version tracking and collaborative workflows like what we'll have to do on our main project, so it's a good idea to get used to it in a lower stakes environment. Even if you delete the entire repository, that's ok :P

## Coding Stuff

The repository contains the data file for the wine dataset. This dataset includes the following columns:<br>
Input variables<br>
1 - fixed acidity<br>
2 - volatile acidity<br>
3 - citric acid<br>
4 - residual sugar<br>
5 - chlorides<br>
6 - free sulfur dioxide<br>
7 - total sulfur dioxide<br>
8 - density<br>
9 - pH<br>
10 - sulphates<br>
11 - alcohol<br>
Output variables<br>
12 - quality (score between 0 and 10)<br>
The dataset does not contain any errors, missing values, or mismatched values.

When actually creating the project, make sure to install the pandas and scikit-learn libraries. Matplotlib may also be useful.

