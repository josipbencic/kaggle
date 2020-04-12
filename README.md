# kaggle


## Setup
1. Install conda
2. checkout the repo
3. create the conda environment from the environment.yml
4. switch to the new, "kaggle" environment
5. start jupyter in the notebooks folder


## Cheat Sheet
### To export the environment
conda env export --from-history > environment.yml

### To import the environment
conda env create --file environment.yml

### Delete current environment
conda env remove --name kaggle

### Activate
conda activate kaggle
