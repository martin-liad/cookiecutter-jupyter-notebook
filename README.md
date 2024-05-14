# Cookiecutter Jupyter Notebook

_A project structure for data analysis projects using Jupyter Notebook._

### [Project homepage](https://github.com/martin-liad/cookiecutter-jupyter-notebook)

## Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## Starting a new project:
------------
To start a new project, `cd` into a directory where you want the new project and run

    cookiecutter https://github.com/martin-liad/cookiecutter-jupyter-notebook.git

## The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── README.md          <- The top-level README for analysts using this project.
├── .gitignore         <- Specify files that are excluded from Git version control.
├── data
│   ├── downloaded     <- Data from downloads.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final data sets for publication.
│   └── raw            <- The original, immutable data files.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt
├── .env               <- Environment variables                          
│
└── *.ipynb            <- Example Jupyter notebooks to get you started
```

## Installing development requirements
------------

    pip install -r requirements.txt
