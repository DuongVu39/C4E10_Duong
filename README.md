# C4E10_Duong




<h1 align="center">

  <br>

rGenius

<br>

</h1>

<h5 align="center">

Created by</a></h5>

<h4 align="center">

Tyler Roberts

Maud Boucherit 

Duong Vu

Tariq Hassan

</a></h4>

<br>

<h4 align="center">



<br>

<h4 align="center">







</a></h4>

<h1></h1>

<h4 align="center">

  Main Features •

  Usage •

  Dependencies •

  Installation •

</h4>

<h1></h1>

<br>

Overview

Genius is a website that allows users to provide annotations and interpretation of song lyrics, news stories, sources, poetry, and other documents.

This R package wraps the Genius API (here) and provides some interesting data extraction.

Add some plots from last labs for demonstration

Main Features

Below are some functions that has been developed in the package:

- get_song()
  - args:
- get_songs()
  - args:
- search_song()
  - args:
- get_artist()
  - args:
- get_song_from_artists()
  - args:

Usage

    get_songs(seq(from=1, to=300), access_token)



Dependencies

- R >= 3.4.3
- dplyr: grammar of data manipulation
- httr: a friendly http package for R 
- readr: Read flat files (csv, tsv, fwf) into R
- glue: Glue strings to data in R. 

Installation from sources

To install the package, simply type the code below in the console:

    devtools::load_all()
    devtools::install_github("tylercroberts/rGenius")



Contributing to rGenius

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

A detailed overview on how to contribute can be found in the contributing guide.

If you are simply looking to start working with the rGenius, navigate to the GitHub “issues” tab and start looking through any issues.

Or maybe through using rGenius you have an idea of your own or are looking for something in the documentation and thinking ‘this can be improved’...you can do something about it!

