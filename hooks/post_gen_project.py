
# ===========
# = Cleanup =
# ===========

import os

# Only include examples that were requested during setup

REMOVE_PATHS = [
    {% if cookiecutter.example_notebooks not in ["basic",   "all"] -%} 'Untitled.ipynb', {% endif %}
    {% if cookiecutter.example_notebooks not in ["mapping", "all"] -%} 'Lewisham ward maps.ipynb', {% endif %}
]

def remove_files(filenames):
  for path in filenames:
      if path and os.path.exists(path):
          if os.path.isdir(path):
              os.rmdir(path)
          else:
              os.unlink(path)

remove_files(REMOVE_PATHS)

# ==================
# = Banner message =
# ==================

def divider():
    print("""

=============================================================================
    """)
    
def conda_env_info():
    print("""
*** Using Conda environments ***

It is recommended that you set up a conda environment for your projects.
The example notebooks are configured to load an environment called
"{{cookiecutter.project_repo_name}}", although you can change this.

You can set this environment up as follows:

Create the Conda environment:
    conda create --name {{cookiecutter.project_repo_name}}
    
Install an ipython kernel so you can launch your notebooks from the base environment:
    conda install --name base nb_conda_kernels
    conda install --name {{cookiecutter.project_repo_name}} ipykernel

Alternatively, to launch notebooks from the project environment only:
    conda install --name {{cookiecutter.project_repo_name}} ipykernel
    python -m ipykernel install --user --name {{cookiecutter.project_repo_name}} --display-name "Python 3 ({{cookiecutter.project_repo_name}})"

Activate the environment before installing dependencies (see below):
    conda activate {{cookiecutter.project_repo_name}}
    """)

def project_info():
    print("""
*** Project setup ***

Navigate to the project directory:
    cd {{cookiecutter.project_repo_name}}

Install the project dependencies:
    pip install --upgrade -r requirements.txt

Launch a Jupyter Notebook server:
    jupyter notebook
    """)

divider()
conda_env_info()
project_info()
