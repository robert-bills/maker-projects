# Python database work  
Using Python to create and populate a database from information in a CSV file.  

There are so many great database products that can be downloaded and evaluated or used for free or a modest fee.  
I made my living as a data engineer for several years and came to appreciate several different offerings.  

## Problem discussion  
The decision to move from a spreadsheet to a database usually stems from either the need for more robust data handling or sharing.  

What prompted me to think about the problem in reverse is the situation where you need to either upgrade or reverse engineer a solution from a product that uses the exact data in your file. Many data handling products have a graphical interface that allow you to prototype and test your solution fairly quickly.  

From this file, I got thinking about a data export that I had from a tool I wrote.  

Moving from a flat sheet to a database solution often involves splitting some data from within a single sheet to multiple sheets to preserve data integrity. We can have a more complete discussion about database strategy another time.  

For now, imagine you want to reverse engineer a simple database from an abandoned project using spreadsheet that's been manually maintained for quite some time.  

We're going to do things the simplest way we can with Python's built-in mechanisms.  

## Determining how to split your data  
looking at your spreadsheet, you can usually find one or more repeating data members. In this solution, we notice that the data being recorded comes from one of a number of sensors.  

A good solution to separate this out would be to create a table to hold the sensor's name and any other data about it and then use a simple value in the list of readings.  

## Why would you do this?  
Let's get this out of the way first: Operationally speaking, there's not much reason to take a single spreadsheet file and use its data to create and populate a database.  

With that said, I have worked in a situation where if the primary database or server was not available, offline storage was created to hold temporary data until it could be integrated into the main solution. From this perspective, we'd absolutely need to create the appropriate schema.  
That's the angle we'll use to justify this exercise.  

## Breaking down the problem  
How would you make a list of the distinct sensor entries from a list?  
One way to do this would be to simply read down the list and transcribe each entry as we encounter it.  

### The manual process  
Think of it this way: start with a blank piece of paper and read your spreadsheet. Do you have this entry on your sheet? If not, write it down, if so, skip it. We'll use this method to make our separate sheet.  

