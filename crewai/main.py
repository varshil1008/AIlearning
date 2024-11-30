from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader('https://www.placid.net/')

page_data = loader.load().pop().page_content
print(page_data)

# llm = ChatGroq(
#     model = 'llama3-8b-8192',
#     api_key='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',
#     temperature=0,
#     max_tokens=None,
#     max_retries=2
# )

# response = llm.invoke('explain the Breast Cancer Screening HEDIS measure, provide a response in JSON with following keys : Denominator, Numerator, Required Exclusion, Optional Exclusion, valuesetcode, clinical code. Include the valueset code & clinical code for each of the categories and the codetype ')

# print (response.content)