import pyspark

def process_data(df):
    """
    Increases salary by 10%.

    Args:
        df (DataFrame): Input DataFrame with 'name' and 'salary'.

    Returns:
        DataFrame: DataFrame with 'name' and 'new_salary'.
    """
    from pyspark.sql.functions import col, expr
    return df.select(
        col('name'),
        (col('salary') * 1.1).alias('new_salary')
    )
