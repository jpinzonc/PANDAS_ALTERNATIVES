# PANDAS ALTERNATIVES IN PYTHON

Run several processes with differnet libraries. The time it takes is estimated over several runs of the same code. 

Here is another interactive site comparing pandas and polars 
    
    https://dash-polars-pandas-docker.onrender.com/speed-comparison

- System: 

    Mackbook Pro 15 Inch, 2019 
        
        Processor: 2.3 GHz 8-Core Intel Core i9
        
        Memory: 16 GB 2400 MHz DDR4
        
        macOS:  Sonoma 14.5 Beta (23F5049f)

____

- Data source: 

    Western Pennsylvania Regional Data Center

    Cumulative Crash Data:
    
    https://data.wprdc.org/dataset/allegheny-county-crash-data/resource/2c13021f-74a9-4289-a1e5-fe0472c89881

    Given the size of the original dataset is larger than normal limit in github, this command can be run from the notebook to download the data and generate files of different sizes: 

                exec(open("get_data.py").read()) 
____

### __POLARS__:

- Documentation 

    https://docs.pola.rs/py-polars/html/reference/dataframe/api/polars.DataFrame.clone.html

- Installation

    !pip install polars

______ 

### __DATATABLE__:

- Documentation 

    https://datatable.readthedocs.io/en/latest/


- Installation 

    !pip install datatable

____
### __MODIN__:

- Documentation 

    https://modin.readthedocs.io/en/stable/

- Installation (with dask)

    !pip install modin

    !pip install "dask[distributed]" --upgrade

- Set up (with dask)

    import os

    os.environ['MODIN_ENGINE'] = 'dask'

    import modin.pandas as md
____

### __VAEX__:

- Documentation 

    https://pypi.org/project/vaex/

    Currently (20240429) Vaex is not supported for python 3.12 (https://github.com/vaexio/vaex/issues/2397)
    
- Installation

    !pip install vaex

    or 

    !conda install -c conda-forge vaex

_____
________
