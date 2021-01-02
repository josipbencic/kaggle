# kaggle


## How to open
1. Navigate to `kaggle`
2. `conda activate kaggle`
3. `jupyter notebook notebooks`


## Setup
1. Install conda
2. checkout the repo
3. create the conda environment from the `environment.yml`
4. switch to the new, "kaggle" environment
5. start jupyter in the notebooks folder


## Cheat Sheet
### To export the environment
`conda env export --from-history > environment.yml`
or if positioned in project root, this also works:
`conda env create`


### To import the environment
`conda env create --file environment.yml`

### Delete current environment
`conda env remove --name kaggle`

### Activate
`conda activate kaggle`
