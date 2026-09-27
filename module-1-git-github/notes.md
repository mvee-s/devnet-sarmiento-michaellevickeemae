# Module 1 — Git & GitHub

**Student:** Michaelle Vickeemae G. Sarmiento
**Date:** September 25, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a tool that runs and keeps track of changes in a project. While, Github is a online platform that can keeps Git repositories.  In a real world scenario, we can think that a pencil is the Git, while the notebook is the Github. With the use of pencil, we can write and erase information. If we write something then realizes something's wrong, we can easily use the eraser to go back to our initial written information. And then, after we write or finish our written information, since it is written in the notebook, we can easily give the notebook to our teacher or classmates for them to see our work and give comments or feedback or correct our information if necessary.

---

## Key vocabulary (in your own words)

- repository: storage
- commit: save changes
- branch: separate workspace
- push / pull: upload and download
- pull request: request for approval
- merge conflict: overlapping work

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]

During our midterm lab exam, we were given a task. and the repository to be used is this (devnet-sarmiento-michaellevickeemae) in Github. To avoid unwanted changes in my initial files, I made a new branch name midterm-movie-collection.

After I made the new branch, I made a new file which is devnet-midterms.py where my lab exam is placed. This ensures that my changes are reflected only in the midterm-movie-collection branch.

While I was working, everytime I accomplish part, I git add and git commit my changes with useful message. After our lab exam, I git push origin HEAD:midterm-movie-collection. This is to ensure that I pushed my changes on the specific new branch I made for midterms.

After that, I went to the main branch and clicked the pull & request and created my pull request with the information needed.

# paste your actual commands here
git add . 
git commit -m "I inputted message here depends on what changes I made"
git push origin HEAD:midterm-movie-collection (this ensures I pushed my changes to the midterm-movie-collection branch. HEAD means the active local branch.)
---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

The mistake I made during those time is not checking if someone is logged in in Git. so when i git add, git commit, and git push, other git and github account was showed. 

So i had to delete my branch and start over again to fix that mistake. I changed then the user details by git config --global user.name and git config --global user.email.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]

From what I understand with the question, version control before to me is like having multiple files in my laptop with changes and different file names like Final1, Final na to, FinalFinal. Yes, it keeps track of my changes, but if I look into it after a few days, I am not sure what changes have I made on those different files. Unlike in Git, I have at least a gist on what I have changed. I can easily go back to that version without checking the whole files and wondering what changes I made before.