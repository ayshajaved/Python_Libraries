'''
In Pandas, the primary data structures are `Series`, `DataFrame`, and `Panel`. These structures are designed to handle different types of data and provide various functionalities to manage and analyze data efficiently. Here's an explanation of each:

### **1. Series**
   - **Definition**: A `Series` is a one-dimensional labeled array capable of holding any data type (integers, strings, floating-point numbers, Python objects, etc.). It is similar to a column in an Excel spreadsheet or a single column in a database table.
   - **Structure**: It consists of two main components:
     - **Values**: The actual data.
     - **Index**: A sequence of labels, which allows for easy access to the data.
   - **Example**:
     ```python
     import pandas as pd

     data = [10, 20, 30, 40, 50]
     series = pd.Series(data)
     print(series)
     ```
     Output:
     ```
     0    10
     1    20
     2    30
     3    40
     4    50
     dtype: int64
     ```

### **2. DataFrame**
   - **Definition**: A `DataFrame` is a two-dimensional labeled data structure with columns of potentially different data types. It can be thought of as a table or a spreadsheet in which each column represents a `Series`, and the `DataFrame` itself is a collection of these `Series`.
   - **Structure**: It consists of:
     - **Data**: The actual data, which can be of various types.
     - **Index**: Row labels.
     - **Columns**: Column labels.
   - **Example**:
     ```python
     data = {
         'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'Salary': [50000, 60000, 70000]
     }
     df = pd.DataFrame(data)
     print(df)
     ```
     Output:
     ```
           Name  Age  Salary
     0    Alice   25   50000
     1      Bob   30   60000
     2  Charlie   35   70000
     ```

### **3. Panel** (Deprecated)
   - **Definition**: A `Panel` was a three-dimensional data structure used in earlier versions of Pandas. It was primarily used to handle data that had three dimensions, such as time series data where each time period had a `DataFrame`.
   - **Structure**: It had three axes:
     - **Items**: The first axis, representing the major axis (e.g., the different `DataFrames`).
     - **Major axis**: The second axis, typically representing the rows of the `DataFrame`.
     - **Minor axis**: The third axis, typically representing the columns of the `DataFrame`.
   - **Example**:
     ```python
     import numpy as np

     data = np.random.rand(2, 4, 3)
     panel = pd.Panel(data)
     print(panel)
     ```

   **Note**: The `Panel` data structure has been deprecated since Pandas version 0.25.0 (July 2019) and was removed in later versions. For three-dimensional data, you should now use the `xarray` package or work with multi-index `DataFrames`.

### **Current Alternative for Panel**
   - **MultiIndex DataFrame**: You can achieve similar functionality as the deprecated `Panel` by using a `DataFrame` with a `MultiIndex` for rows or columns, allowing for more complex data representations.
   - **xarray**: A package designed for working with multi-dimensional arrays, which can serve as a modern replacement for `Panel`.

### **Summary**
- **Series**: 1D, similar to a single column.
- **DataFrame**: 2D, similar to a table with multiple columns.
- **Panel**: 3D (deprecated), was used for handling more complex data but is now replaced by alternatives like `xarray` and MultiIndex `DataFrame`.
'''