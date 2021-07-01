# Star Wars Image Scraper

## Description

This is a proof-of-concept scraper, in python, that scrapes images from wookieepedia corresponding to items in the swapi API.

## Features

- running `extract_categories.py` will obtain the list of items grouped by categories e.g. people, vehicles, planets etc. from the swapi API, and output it in json to an output text file `output.txt`

- running `extract_images.py` will deserialize the output file from previous step into a python object containg the categories and their items
  - using selenium, it will then search the wookieepedia website to download the image that corresponds to each category item, using the search term associated with each item
  - it does this for each category item, looping through all categories. 
  - all images are downloaded to the `images` folder
  - finally, extract-images.py will log a list of items for which it was unable to download any images for, and output in json format to a output text file `empty-images.txt` 

- the selenium program uses adblocker to minimise disruption to the DOM when running the selenium script
- also searches directly for each item using the url instead of navigate back to the search page
- total runtime is about 20 mins for about 200+ images

## Installation

1. Clone this repository
2. Create a virtual python environment using `venv`
3. Activate the virtual environment by navigating to the virtual environment's scripts folder and executing the `activate.bat` file
4. `pip install -r requirements.txt` to download all third-party packages
5. Run `extract_categories.py` first
6. Next, run `extract_images.py`

## Potential Improvements 

- To eliminate instances of false negatives i.e. empty images whether there should be images 
- To eliminate instances of false positives i.e. images that do not correspond correctly to the associated item


