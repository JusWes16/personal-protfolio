# Overview

This is my portfolio that I have made containing a little about me as well as a few different projects that I have done. 
To run the app first start by running npm install to ensure that you have all of the requiured packages for this app to run.
The type in the terminal, nodemon app.js. This will launch the site served from your local computer. To view the site type into the address bar 
in your browser, http://localhost:3000. There will also be a link in the terminal after the app is lanched. The purpose of this app
Was to not only provide a location for others to view my work and learn more about me but also to demonstrate my skills in Node.js, express, and EJS.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

I have three pages in my web app. The first is the home page where you can find and little greeting heading as well as
a short about me section and a section my my current experience. My name, contact info in the header, and the about me section 
are all created by importing data from a JSON file containing that information. The about me page is the same as the about me 
section however it contains a picture and gives me a place to add to my about me in the future. The final page is the projects page. 
This page contains a list of projects that I have done in the past. Each has the name of the projects the language it was written in and a 
link to the code on my GitHub. Each project card is dynamically made by looping through an array of objects and printing the appropriate 
infomation for each. 

# Development Environment

Visual Studio Code

JavaScript / Node.js
* Express
* Path module
* Body Parser module
* Nodemon

# Useful Websites

* [Stack Overflow](https://stackoverflow.com/)
* [Node.js](https://nodejs.org/dist/latest-v14.x/docs/api/)
* [Express](http://expressjs.com/)
* [w3schools](https://www.w3schools.com/nodejs/nodejs_intro.asp)

# Future Work

* Add more projects
* Improve search functionality and security
* Add to my about me page
* Add additional pages for experience (once I get it)