def project_info():
    print("""

=============================================================================

*** How to get started ***

Create a Conda environment for your project:
    conda create --name {{cookiecutter.project_repo_name}}
    
Install an ipython kernel for this environment:
    conda deactivate
    python -m ipykernel install --user --name {{cookiecutter.project_repo_name}} --display-name "Python 3 ({{cookiecutter.project_repo_name}})"

Activate the environment:
    conda activate {{cookiecutter.project_repo_name}}
    
Navigate to the project directory:
    cd {{cookiecutter.project_repo_name}}

Install the project dependencies:
    pip install -r requirements.txt
    conda install nb_conda_kernels

Launch a Jupyter Notebook server:
    jupyter notebook
    """)

project_info()
