# Design
A blog mock command line tool
## Description
A blog type app writen in python3

<!-- Images -->
![Blog Ocon](https://images.pexels.com/photos/459688/pexels-photo-459688.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)

# Features
### Users:
<!-- UL -->
* Users come in 3 roles: normal users, moderators, and admins. 
* Normal users can only create new comments, and edit their own comments.
* Moderators have the added ability to delete comments (to remove trolls), while admins have the ability to edit or delete any comment.
* Users can log in and out, and we track when they last logged in
 
### Comments:
* Comments are simply a message, a timestamp, and the author.
* Comments can also be a reply, so we'll store what the parent comment was.



## Requirements
1. python 3
2. git

## Contibute
<!-- Code Blocks -->
```bash
 git clone https://github.com/CryceTruly/Design.git

 cd Design 

 python comments.py

```