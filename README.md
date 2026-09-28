# lab04-Dune
192-211 Automated Software Testing


## Group Name - Dune



## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Minn Khant Si Thu | minnkhantsithu | test_teardown.py |
| Nyi Sett | Wha1e0134 | test_withdraw.py |
| Soe Moe Hein | 6705142013-SoeMoe | test_shared.py |
| Swam Pyae Paing | LoneKit | conftest.py |
| Thet Htoo Aung | thethtoo724-design | test_deposit.py |



### Our Merge Conflict

During Round 3, our group experienced a merge conflict while working on the README.md file. Different members edited the same section of the file at the same time. Git therefore marked the conflicting changes using conflict markers.

The conflict appeared in the following form:

```text
<<<<<<< HEAD
| Member A | GitHub Username | test_withdraw.py |
=======
| Member B | GitHub Username | test_deposit.py |
>>>>>>> commit
```

After reviewing the changes, our team decided to keep the correct contribution information from all five members. The final Who Did What table was:

| Member | GitHub Username | File |
|---|---|---|
| Minn Khant Si Thu | minnkhantsithu | test_teardown.py |
| Nyi Sett | Wha1e0134 | test_withdraw.py |
| Soe Moe Hein | 6705142013-SoeMoe | test_shared.py |
| Swam Pyae Paing | LoneKit | conftest.py |
| Thet Htoo Aung | thethtoo724-design | test_deposit.py |

We removed the conflict markers, combined the valid information, and committed the resolved README.md.

Git could not automatically resolve the conflict because different members had changed the same part of the README at the same time. Git could identify that the versions were different, but it could not determine which information the team wanted to keep. Therefore, we had to review the changes and resolve the conflict manually.

Important: If you want to show the exact conflict, replace the example conflict block with the exact <<<<<<< ... ======= ... >>>>>>> lines that actually appeared in your terminal. That is stronger evidence for the assignment's Round 3 requirement.



### Git Contribution Summary
    
    Output of "git shortlog -sn"

    15  SwamPyaePaing
    13  Soe Moe Hein
    12  Wha1e0134
     6  Minn Khant Si Thu
     5  thethtoo724-design


### Reflection Questions

1. **Why was your push rejected, and how did you fix it?**
   My push was rejected because there were new changes on GitHub that I did not have on my computer. I used `git pull`, fixed the README conflict, and then pushed again.

2. **Why could Git not resolve the README conflict automatically?**
   Git found changes in the same part of the README from different people. It could not know which one we wanted to keep, so I fixed it myself.

3. **What is the difference between committing and pushing?**
   Committing saves my changes on my computer. Pushing sends my commits to GitHub.

4. **How do fixtures reduce duplicated setup code in tests?**
   Fixtures let us prepare something once and use it in different tests. This means we do not have to write the same setup code again and again.

