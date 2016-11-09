---
layout: post
title: "Introduction"
date: 2016-10-15
---

I am not a software developer. 

My day job is managing data and innovation for an archaeological services business. It faces many of the introverted challenges of a medium sized business, including organising information and achieving consistency between different departments/projects/offices. This makes it a very interesting place for someone like me, who enjoys finding ways of making information more intuitive to gather and more useful. My role is typical of a departmental manager - administration, diplomacy, delegation, promoting and juggling, with only a small sliver of focused personal productivity. More on this another time.


To cut to the chase, our field teams produce a lot of survey data using GPS and total stations. This data represents a primary spatial record for an archaeological site and it is important that is gathered correctly, and made available to anyone who needs it in a useful format. It also has to be checked for both survey and archaeological errors, as well as completion and detail. The raw data is exported presently as a `.csv` comma separated text file, which must be processed to turn it into useful CAD information. I wrote a little software tool some years ago that automates most of the survey processing. It is called the *GPS Muncher* and has the following positive characteristics:

* it has a simple, totally intuitive interface (drag a `.csv` file into a box and it works)
* it can inform the user of most survey coding errors
* it outputs a `.scr` script file which can be readily dropped into any CAD software
* it can deal with large data sets > tens of thousands of lines

The *GPS Muncher* has seen intensive use over the past years and has been remarkably reliable in the hands of a wide variety of people, often with almost no training. It has also avoided the excessive cost of commercial software licenses, and allowed us to tailor the results to the needs of the company specifically. However, with a sharp increase in the volume of survey data expected in the coming years, and increasingly wide exposure to new staff, it is time to review and update the software. 

The purpose of this written record is to describe the process of designing and developing an improved survey data processing tool. This is useful as basic documentation and perhaps of interest as a story of an amateur software developer attempting to produce robust and intuitive business software. Necessarily, this text will be at once fluffy and highly specific, structured and disorganised, and it is unlikely to be profound. The exercise of writing it will be fun, and will give me a reason to be somewhat methodical in my approach. It will also be interesting to see how much my ideas about what, how, where and when and who change over the course of the project.

Incidentally, the choice of *Markdown*  to prepare this document is also a test. The potential for using a form of *Markdown* or *LaTeX* for removing the distraction and inconsistency of preparing technical reports in *Microsoft Word* is certainly worth revisiting.

#####Back to the nitty gritty

The following issues have been highlighted with the tool's basic functionality:

* it cannot function if the `.csv` file is still open in other software, which slows down any editing
* it can get stuck on certain sets of data for no evident reason, requiring that data to be moved to the end of the file
* it can be laborious to fix long lists of errors
* large `.scr` files can get stuck in CAD software and need to be split up
* only I can fix it 

There are also a number of opportunities to enhance the functionality of the software, to improve ease of use and produce more useful results:

* the software could fix a large proportion of coding errors automatically
* the software could audit the data and:
	* correct naming errors, grouping together any that are unclear
	* understand what the data represents and check that naming and coding are appropriate
	* produce an index of trenches, contexts &c that are present
	* produce a measure of survey quality and comments as feedback to the surveyor(s)
* the software could produce coloured line work in CAD as per our conventions
* alternate layer naming conventions (geometry together or contexts together)
* the software could offer alternate outputs:
	* direct output to `.dxf` to avoid the step of using the `.scr` and performance issues that brings
	* direct output to a suitable set of `.shp` files for use in GIS
	* direct output to a spatial database
* the software could prepare further contextual information - areas, volumes or sheets of section views
* the software could be accessed from a more useful location, e.g. as a *QGIS* plugin or web-based tool

#####Where to begin?

The original *GPS Muncher* was written in 2010 using *Microsoft Visual Basic .NET*. This was easy to distribute on an entirely *Windows*-based company and fell best within my programming comfort zone. The logic was very simple - read a `.csv` file line by line and convert into appropriate text for an `.scr` file. The previous two lines were checked to build in some resilience to coding errors - which were then reported in an external text file, requiring correction and re-processing. The software had no awareness of what sort of archaeological data it was processing and so could only undertake limited quality control. Structurally, the code also became pretty ugly - it was written in one large procedure with no modularity and so is very difficult to modify without potentially breaking something unexpected. This also restricted the potential for anyone but the original developer to alter the code.

The new survey data processor must be built to a higher standard of programming, which to the author presently means:

* more modular code to isolate unrelated processes and improve re-usability and expandability
* complete separation of logic from interface
* more elegant handling of data internally 
* improved documentation and accessibility to the code

In principle, *Visual Basic .NET* is still a good fit as a development platform, as the business remains Windows-centric. However, the author is also considering *Python*, which promotes clean code and would allow possible integration with *QGIS*, *Agisoft Photoscan* and other frequently used software tools. Another possibility is a web-based system, possibly using *Javascript* to make the tool totally portable, although integration into local file systems and desktop software would then be more difficult.


**Structure**

Here follows a basic chart showing the flow of data through the software:

```flow
st=>start: Read data
e=>end: Output data
op1=>operation: Store input data
op2=>operation: Organise data
op3=>operation: Correct data
op4=>operation: Prepare output data
op5=>operation: Store output data

st->op1->op2->op3->op4->op5->e
```

Each of these boxes has a number of potential options:

stage     						| possible functions
------------------------	| ---
Read data  					| from `.csv`; `.xml`; other Trimble/Leica formats; incremental updating
Store input data  			| internal array; external file; database
Organise data      		| separation into blocks; understanding block type; registering block;
Correct data					| correcting coding and naming; handle multiple blocks; dealing with unclear data
Prepare output data		| preparing drawing data; preparing additional data; tidied original data
Store output data 		| internal array; external file; database
Output data					| drawing data to `.scr`, `.dxf`, `.shp`; error data; additional data; registers

**Other loose ideas**

* Consider specific object types for blocks - contexts, drawings, etc
	* *context* object could hold: 
		* *number* (integer)
		* *extent* (WKT string) 
		* *section* (WKT string)
		* *base* (WKT string)
		* *level* (WKT string)
		* *other* (WKT string)

Clearly there is a lot of work here - how best to structure development to make the most useful gains quickly?
