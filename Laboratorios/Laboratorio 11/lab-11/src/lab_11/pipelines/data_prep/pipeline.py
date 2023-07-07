"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_data, preprocess_companies, preprocess_shuttles, create_model_input_table

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=get_data,
            inputs="datasets",
            outputs="outputs",
            name="get_data"
        ),
        node(
            func=preprocess_companies,
            inputs="companies",
            outputs="companies_preprocessed",
            name="preprocess_companies"
        ),
        node(
            func=preprocess_shuttles,
            inputs="shuttles",
            outputs="shuttles_preprocessed",
            name="preprocess_shuttles"
        ),
        node(
            func=create_model_input_table,
            inputs="companies_shuttles_reviews",
            outputs="model_input_table",
            name="create_model_input_table"
        )
    ])
