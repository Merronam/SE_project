Functions available in the module
---------------------------------

.. py:function:: col_names(data)

        Adds column names. Assumes odd columns are coordinates and even columns are
        energy values. Only first column gets "Coord" name, the rest are left 
        nameless. The energy columns are names "USX" where X is 10, 20, 30, etc.

        :param data: Dataset that contains US runs
        :type data: pandas.DataFrame
        :return: Data with column names and list of column names (without Coord)



