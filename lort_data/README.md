# Overview

The software that I wrote here is a little demonstration of how to use SQL along with Python to perform CRUD operations to a database. The database that I have created and 
that users are interacting with is a database of Lord of the Rings characters. This is a simple program that asked for user input to know what operations to perform. By entering 
a value between 1 and 5 you can perform different CRUD operations to the database. Entering 6 will exit the program and anything other than 1 through 6 will prompt and error message.

The purpose of this program really is to demonstrate how to use SQL and basic Python the create a simple, easy to use database system. Although the way I have written this program 
is based around The Lord of the Rings, it can be implemented for any database for keeping track of individual people, for example, members of a family, members of a club or team, 
or tenants at an apartment complex.

[Software Demo Video](https://youtu.be/6zbi6HQW4RA)

# Relational Database

I am using a simple one table database using Python and SQLite3 to store and access values from a local file.

The structure is very simple. There is only one table which can hold any number of character data. Each entry requires a name, a race, the characters current life status, and a url for 
an image of the character. Each of these values has a data type of text. 

# Development Environment

VSCode

Python 
SQLite3

# Useful Websites

* [Python Geeks](https://pythongeeks.org/)
* [YouTube](https://www.youtube.com/watch?v=pd-0G0MigUA&ab_channel=CoreySchafer)
* [Stack Overflow](https://stackoverflow.com/)
* [Python](https://www.python.org/doc/)
* [W3Schools](https://www.w3schools.com/python/)

# Future Work

* Expand the database to include more than one table 
* Add more functionality for the user to make changes to the database
* Add some sort of GUI to improve the user experience
