
examples = [
{
    "input": "List all the SKUs sold by Imperial in 0015I00000OYJeHQAX",
    "query": "SELECT DISTINCT [product_identity], [product_name] FROM sales_data_en WHERE [outlet_id] = '0015I00000OYJeHQAX' AND [product_identity] IN ( SELECT [product_identity] FROM product_data_en WHERE [manufacturer_group] = 'Imperial') ORDER BY [product_identity] ASC;"
},

]

from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
import streamlit as st
import library as lib


def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        lib.get_embedding_model(),
        Chroma,
        k=2,
        input_keys=["input"],
    )
    return example_selector