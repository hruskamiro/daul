# -*- coding: utf-8 -*-
# Copyright (c) 2023 Miroslav Hruska

#%%
def intro_constructive():
  """
  <intro:1>
  
  Let us have a :class:`~pandas.DataFrame` with a simple content.  
  
  >>> import pandas as pd  
  >>> adf = pd.DataFrame({'x': [0, 1]})  
  >>> adf
     x
  0  0
  1  1

  Now, using the utils in :mod:`daul.pandas_utils`, we will 
  constructively update the column, meaning that we will create a new
  frame with the updated column. 
    
  >>> from daul import pandas_utils as pdu
  >>> bdf = pdu.update_column(adf, 'x', adf['x'] + 1)

  Now, let us take a look at the frame `bdf`: 

  >>> bdf
     x
  0  1
  1  2
  
  We see that `bdf` has the desired content.   
  
  Note, however, that `adf` remains the same.   
  
  >>> adf
     x
  0  0
  1  1
  
  As this update operation is common, it is also part of the
  :mod:`daul.shortcuts` module. 
  
  >>> from daul import shortcuts as ds
  >>> cdf = ds.pduc(adf, 'x', adf['x'] + 2)
  >>> cdf
     x
  0  2
  1  3

  When implementing some functionality, we often see a series of 
  such assignments. 
  
  For instance: 
  
  >>> ddf = adf  
  >>> ddf = ds.pduc(ddf, 'x', ddf['x'] + 1)
  >>> ddf = ds.pduc(ddf, 'y', ddf['x'] * 2)
  >>> ddf
     x  y
  0  1  2
  1  2  4
  
  Note, however, that `adf` still remains the same: 
  
  >>> adf
     x
  0  0
  1  1
  
  </intro:1>
  """
  
  
#%% 
if __name__ == "__main__":
  import doctest
  doctest.testmod()
