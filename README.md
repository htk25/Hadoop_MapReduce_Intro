# Hadoop_MapReduce_Intro
This repository contains Python scripts for the Introduction to Hadoop and MapReduce course by Cloudera at Udacity

# Lesson 6 Project[Optional]
1. Sales per Category

  Solution: 

    code/Lesson6_Project_1/mapper_Q1.py 

    code/Lesson6_Project_1/reducer_Q1.py

2. Highest Sale

  Solution: 

    code/Lesson6_Project_1/mapper_Q2.py 

    code/Lesson6_Project_1/reducer_Q2.py

3. Total Sales

  Solution: 

    code/Lesson6_Project_1/mapper_Q3.py 

    code/Lesson6_Project_1/reducer_Q3.py

4. Hits to Page

  Solution: 

    code/Lesson6_Project_1/mapper_Q4.py 

    code/Lesson6_Project_1/reducer_Q4.py

5. Hits from IP

  Solution: 

    code/Lesson6_Project_1/mapper_Q5.py 

    code/Lesson6_Project_1/reducer_Q5.py

6. Most Popular

  Solution: 

    code/Lesson6_Project_1/mapper_Q6.py 

    code/Lesson6_Project_1/reducer_Q6.py


# Lesson 8 Final Project

# Notes

1. scp -r(recursive flag, optional) training@[IP addr]:/home/training/udacity_training/code [local directory], this command for copying from the remote to local in SSH.
2. head -50 input.txt | mapper.py | sort | reducer.py, for small dataset testing. 50 is just an arbitrary small number.
3. edit etc/vimrc or etc/vim/vimrc for vim global setting

# Resources

1. File transfer between local and remote in SSH: https://docs.google.com/document/d/1MZ_rNxJhR4HCU1qJ2-w7xlk2MTHVqa9lnl_uj-zRkzk/pub
2. Outdated course wiki: https://www.udacity.com/wiki/ud617#setting-up-the-vm-datasets
