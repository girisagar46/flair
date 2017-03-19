# flair

## wtf is it ?
Flair is a simple app build in flask and hosted in [Heroku](https://heroku.com/). Flair can be used to view the final year project documents of the students of batch 2016 from Deerwalk Institute of Technology.

## Is it online ?
Absolutely. Access directly from here [https://flair16.herokuapp.com/](https://flair16.herokuapp.com/)

The index page displays paper title, name of student and abstract of the paper. On clicking "View Paper" button, user can view the pdf of the document and download it as well. 

This app is just a tryout for me to learn flask app and deploying to Heroku. There are lot's of error and violations of PEP8 conventions. ;-) 

## Anythning I should know ?
The contents displayed in the index page is loaded via a static CSV file. Datatable is used to render those contents. To display the document pdf, [pdf.js](https://mozilla.github.io/pdf.js/) is used.

All the documents are hosted in [Github](https://github.com/CSIT-GUIDE/FYP-2016) hence app uses Github API to access those pdf's for displaying.

# Contribute
I haven't really thought of including contribution yet.

# Resources
If you dont want to access all the PDF's then you can visit: [https://github.com/CSIT-GUIDE/FYP-2016](https://github.com/CSIT-GUIDE/FYP-2016)

For all the CSIT releated content, visit: [https://github.com/CSIT-GUIDE/](https://github.com/CSIT-GUIDE/)