# Reportal
This is our submission for the SUP Free hackathon by Crowdpolicy

## Technologies Used:
The website is build with **Django** in **Python**, it also used **HTML**, **CSS** and **Javascript**.
Insite the **Site** files you can find the HTML files in the **templates** directory, and in the **static** directory you can find the **css**,**js** and images

There is a function in the site to upload and register a bin. To do that the coordinates are taken with the Google Maps API and the the phot is processed with a Convolutional Neural Network. First the object detection happens to locate the bin in the image, then another Convolutional Network makes the classification if the bin is garbage or recycle.
There is another Concolutional Network that classifies materials in 6 categories
* Paper
* Glass
* Cardboard
* Trash
* Plastic
* Metal


## Installation Guidelines:
* To run the AI notebook it is recommend it to run it in Google Colab if you don't have a GPU
* To run the server/website, you need to install Django and Python, preferably on Linux and the inside the **site** directory run **python manage.py runserver**.
Then visit **localhost** address in your browser.

Datasets Used:
1) Materials dataset from Stanford University: https://github.com/garythung/trashnet/tree/master/data
2) Recylable materials from data.world (CSV): https://data.world/buffalony/ru4s-wz29/workspace/file?filename=recyclable-materials-1.csv
3) Bin classification is a dataset that I started and want to update it and evolve it, now it has ~50 images of garbage and recycle bins. I will post the link to my repo where I plan to update it for whoever wants to use it: https://github.com/ichamatidis/RePortal/tree/main/Recycle%20Vs%20Garbage%20Bins
