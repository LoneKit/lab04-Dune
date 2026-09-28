# lab04-Dune

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Minn Khant Si Thu | minnkhantsithu | test_teardown.py |
| Nyi Sett | Wha1e0134 | test_withdraw.py |
| Soe Moe Hein | 6705142013-SoeMoe | test_shared.py |
| Swam Pyae Paing | LoneKit | conftest.py |
| Thet Htoo Aung | thethtoo724-design | test_deposit.py |


### Our Merge Conflict

We had a merge conflict in the `README.md` file because my changes and another member's changes were made in the same part of the file. Git could not decide which changes to keep, so it showed conflict markers like `<<<<<<<`, `=======`, and `>>>>>>>`. I checked the changes, kept the information we needed, removed the conflict markers, and then committed the fixed README.


### Reflection Questions

1. **Why was your push rejected, and how did you fix it?**
   My push was rejected because there were new changes on GitHub that I did not have on my computer. I used `git pull`, fixed the README conflict, and then pushed again.

2. **Why could Git not resolve the README conflict automatically?**
   Git found changes in the same part of the README from different people. It could not know which one we wanted to keep, so I fixed it myself.

3. **What is the difference between committing and pushing?**
   Committing saves my changes on my computer. Pushing sends my commits to GitHub.

4. **How do fixtures reduce duplicated setup code in tests?**
   Fixtures let us prepare something once and use it in different tests. This means we do not have to write the same setup code again and again.



