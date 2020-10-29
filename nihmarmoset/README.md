# nihmarmoset - Data Science Repo for NIH Marmoset Project
==============================

## Quickstart

First follow setup according to the desired system.  Of particular note, make sure that your `.env` file is set to 
reflect the file-paths on your system.  For example, on his laptop, John has his set to:
```
# Environment variables go here, can be read by `python-dotenv` package:
#
#   ----------------------------------------------------------------
#    from dotenv import find_dotenv, load_dotenv
#
#    load_dotenv(find_dotenv())
#   ----------------------------------------------------------------
#
# DO NOT ADD THIS FILE TO VERSION CONTROL!
CONTAINER=cdean1/mindpy:0.1
PROJECT_ROOT=/Users/fisher/projects/NIH/git/nihmarmoset
PROJECT_DATA=/Volumes/JWFExtDat/data/marmoset/data
PROJECT_MODELS=/Volumes/JWFExtDat/data/marmoset/models
PYTHONPATH=/usr/local/lib:./:/Users/fisher/projects/NIH/git/nihmarmoset/src
PYTHONUBUFFERED=1
# Pass the timezone to tzdata on the container to match the host.  Set it to the
# value returned by `ls -la /etc/localtime | cut -d/ -f8-9` on the host.
TZ=America/New_York
```
## Setup Instructions

Note that these are not complete. I am providing the `venv` setup approach, but others use Anaconda, docker, etc. This 
will need updating.

### VENV Setup (local)

Assumes that you have *already* cloned the repo. The example commands follow John's local setup (i.e. your directories 
are probably different)

1. Navigate to the directory where you cloned the repo

   ```
   cd ~/projects/NIH/git/nihmarmoset
   ```

2. Create a `venv` environment (see [python venv](https://docs.python.org/3/library/venv.html) for more information.)

   ```
   python -m venv venv
   ```

   This will create a subdirectory name `venv` in your git repo. Tools like `pycharm` will automatically detect `venv` 
environments and activate them automatically. If you are using a different IDE, you may need to activate manually. Note
that you can change the name of the subdirectory, *but* you will have to add it to `.gitignore` so that it does not get
tracked by git (which would result in cluttering everyone else's copy of the repo).

3. With the `venv` environment active, install the project requirements:
    ```
    pip install -r requirements.txt
    pip install -e .
    ```
   Older instructions included `pip install -r requirements.txt`, but if required packages are listed in `setup.py` then
   `pip install -e .` it isn't necessary. There is an open question on how to manage package dependencies since the list
   of required packages will evolve as code is developed and there are *better* ways to detect which packages are being
   loaded by code within the repo.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
