from typing import Tuple

from pyspark.sql import DataFrame
import pyspark.sql.functions as F


def get_product_category_info(df_products: DataFrame,
                              df_categories: DataFrame,
                              df_link_product_categories: DataFrame
                              ) -> Tuple[DataFrame, list[str]]:
    """
    Returns product–category name pairs and a list of products without categories.

    Args:
        df_products (DataFrame): DataFrame containing product information.
        df_categories (DataFrame): DataFrame containing category information.
        df_link_product_categories (DataFrame): DataFrame mapping products to categorize.

    Returns:
        Tuple[DataFrame, list[str]]:
            - DataFrame of (product_name, category_name) pairs.
            - List of product names without any associated category.
    """
    df_joined: DataFrame = (
        df_products
        .join(df_link_product_categories,
              on="product_id",
              how="left"
              )
        .join(df_categories,
              on="category_id",
              how="left")
    )

    df_product_category_pairs: DataFrame = (
        df_joined.select("product_name",
                         "category_name"
                         )
    )

    df_product_without_category: DataFrame = (
        df_joined
        .where(F.col("category_id").isNull())
        .select("product_name")
        .distinct()
    )

    product_list_without_category: list[str] = \
        [row["product_name"] for row in df_product_without_category.collect()]

    return df_product_category_pairs, product_list_without_category
