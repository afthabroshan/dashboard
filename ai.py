# # import pandas as pd
# # import os
# # import openpyxl
# # from langchain.docstore.document import Document
# # from langchain_community.vectorstores import Chroma
# # from langchain_community.embeddings import HuggingFaceEmbeddings
# # from langchain_community.llms import HuggingFaceHub
# # from langchain.chains import RetrievalQA

# # # --- 1. Load and Process Your Specific CSV Data ---

# # # Define the path to your CSV file
# # file_path = 'OBS_dashboard.xlsx'

# # # Use a try-except block to handle potential file errors
# # try:
# #     # 1. Load the entire workbook
# #     workbook = openpyxl.load_workbook(file_path, data_only= True)

# #     # 2. Select the active worksheet
# #     # You can also select by name: sheet = workbook['Sheet1']
# #     sheet = workbook.active

# #     print(f"✅ Successfully loaded '{file_path}'. Reading rows...")

# #     # 3. Iterate through each row in the sheet
# #     for row in sheet.iter_rows(values_only=True):
# #         # 'row' is a tuple containing all cell values for that row
# #         # (e.g., ('BrandA', 1, 'PN123', 'Widget', 100, ...))
# #         print(row)

# # except FileNotFoundError:
# #     print(f"❌ Error: The file '{file_path}' was not found.")
# # except Exception as e:
# #     print(f"❌ An error occurred: {e}")

# # # Convert each row into a LangChain Document
# # docs = []
# # for index, row in df.iterrows():
# #     # --- IMPORTANT: UPDATE THESE COLUMN NAMES ---
# #     # Make sure these column names match your CSV file exactly.
# #     try:
# #         item_description = (
# #             f"Item with part number '{row['Part number']}' from brand '{row['brand']}', named '{row['name']}', "
# #             f"has an initial purchase stock of {row['purchase stock']}. "
# #         )

# #         branch_stocks = (
# #             f"Stock at branches: MTR is {row['mtr: branch']}, Bahrain is {row['bahrain: branch']}, "
# #             f"Oman is {row['oman: branch']}, APEX MAIN LAND is {row['APEX MAIN LAND: branch']}, "
# #             f"and APEX JAFZA is {row['APEX JAFZA: branch']}. "
# #         )

# #         summary = (
# #             f"The total balance quantity is {row['Balance quantity']}, total sale is {row['sale']}, "
# #             f"total stock is {row['stock']}, and the overall sale percentage is {row['sale %']}%."
# #         )

# #         content = item_description + branch_stocks + summary
# #         # Create a Document object for each processed row
# #         doc = Document(page_content=content)
# #         docs.append(doc)
# #     except KeyError as e:
# #         print(f"⚠️ Warning: Column {e} not found in the CSV. Please check your column names. Skipping row {index + 2}.")
# #     except Exception as e:
# #         print(f"⚠️ An error occurred at row {index + 2}: {e}")


# # print(f"Processed {len(docs)} rows from the CSV.")

# # # --- 2. Create Embeddings and Store in a Vector Database ---

# # # This part remains the same. It converts your text into vectors.
# # embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
# # vector_store = Chroma.from_documents(documents=docs, embedding=embeddings)
# # print("✅ Vector store created.")

# # # --- 3. Set up the LLM and RAG Question-Answering Chain ---

# # # Make sure to set your Hugging Face API token as an environment variable
# # # In your terminal: export HUGGINGFACEHUB_API_TOKEN='your_hf_token'
# # if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
# #     print("❌ Error: Hugging Face API token not found in environment variables.")
# # else:
# #     # Initialize the Language Model
# #     llm = HuggingFaceHub(
# #         repo_id="google/flan-t5-large",
# #         model_kwargs={"temperature": 0.1, "max_length": 512}
# #     )

# #     # Create the RAG chain
# #     qa_chain = RetrievalQA.from_chain_type(
# #         llm=llm,
# #         chain_type="stuff",
# #         retriever=vector_store.as_retriever()
# #     )
# #     print("\n🚀 RAG chatbot is ready to answer questions about your data!")

# #     # --- 4. Ask Questions! ---
# #     # Try asking questions based on the columns you have.
# #     question1 = "What is the sales percentage for the item at the main branch?" # Modify this question
# #     answer1 = qa_chain.invoke(question1)
# #     print(f"\n❓ Question: {question1}")
# #     print(f"✅ Answer: {answer1['result']}")

# #     question2 = "How much stock is there for items in the electronics category?" # Modify this question
# #     answer2 = qa_chain.invoke(question2)
# #     print(f"\n❓ Question: {question2}")
# #     print(f"✅ Answer: {answer2['result']}")

# import os
# import openpyxl
# from dotenv import load_dotenv
# from langchain.docstore.document import Document
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
# from langchain_community.llms import HuggingFaceHub
# from langchain.chains import RetrievalQA

# # --- 1. Load and Process Data Directly from Excel ---
# load_dotenv()
# file_path = 'OBS_dashboard.xlsx'
# docs = [] # This list will hold the text for the chatbot

# try:
#     # Load the workbook, ensuring formulas are calculated
#     workbook = openpyxl.load_workbook(file_path, data_only=True)
#     sheet = workbook.active
#     print("✅ Successfully loaded the Excel file.")

#     # Read the first row to use as column headers
#     headers = [cell.value for cell in sheet[1]]
#     print(f"🕵️  Found headers: {headers}")

#     # Loop through all data rows (starting from the second row)
#     for row_values in sheet.iter_rows(min_row=2, values_only=True):
#         # Create a dictionary for the current row (e.g., {'brand': 'APT', 'sale': 2})
#         row_dict = dict(zip(headers, row_values))

#         # --- IMPORTANT: Customize This Section ---
#         # Check if the row is empty and skip it
#         if not any(row_dict.values()):
#             continue

#         # Use the headers you see printed above to build your text.
#         # .get(key, 'N/A') is a safe way to prevent errors if a cell is empty.
#         try:
#             item_description = (
#                 f"Item with part number '{row_dict.get('PART NUMBER', 'N/A')}' from brand '{row_dict.get('Brand', 'N/A')}', named '{row_dict.get('NAME', 'N/A')}', "
#                 f"has an initial purchase stock of {row_dict.get('PURCHASE STOCK', 0)}. "
#             )
#             branch_stocks = (
#                 f"Stock at branches: MTR is {row_dict.get('MTR', 0)}, Bahrain is {row_dict.get('BAHRAIN', 0)}, "
#                 f"Oman is {row_dict.get('OMAN', 0)}, APEX MAIN LAND is {row_dict.get('APEX        MAIN LAND', 0)}, "
#                 f"and APEX JAFZA is {row_dict.get('APEX JAFZA', 0)}. "
#             )
#             summary = (
#                 f"The total balance quantity is {row_dict.get('BALANCE QTY', 0)}, total sale is {row_dict.get('SSALE', 0)}, "
#                 f"total stock is {row_dict.get('STOCK', 0)}, and the overall sale percentage is {row_dict.get('SALE %', 0)}%."
#             )
#             # print("this is the part number:", item_description),
#             # print("this is the branch stocks:", branch_stocks),
#             # print("this is the summary:", summary),
#             # Combine all parts into a single text document
#             content = item_description + branch_stocks + summary
#             docs.append(Document(page_content=content))

#         except Exception as e:
#             print(f"⚠️ Warning: An error occurred while processing a row: {e}. Skipping row.")
#             continue

# except Exception as e:
#     print(f"❌ An error occurred: {e}")
#     exit()


# print(f"✅ Processed {len(docs)} rows for the RAG chatbot.")

# # Check if any documents were created before proceeding
# if not docs:
#     print("❌ Halting: No data was processed. Check if the Excel file is empty or headers are mismatched.")
#     exit()

# # --- 2. Create Embeddings and Store in Vector Database ---

# print("⏳ Creating embeddings and vector store...")
# embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
# vector_store = Chroma.from_documents(documents=docs, embedding=embeddings)
# print("✅ Vector store created.")

# # --- 3. Set up and Run the RAG Chatbot ---

# if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
#     print("❌ Error: Hugging Face API token not found. Please set it as an environment variable.")
# else:
#     endpoint = HuggingFaceEndpoint(
#         repo_id="inclusionAI/Ling-1T",
#         task="text-generation" # Chat models use the text-generation task
#     )

#     # Then, wrap the endpoint in the ChatHuggingFace class
#     llm = ChatHuggingFace(llm=endpoint)

#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         chain_type="stuff",
#         retriever=vector_store.as_retriever()
#     )
#     print("\n🚀 RAG chatbot is ready! Ask questions about your data.")

#     # --- 4. Ask Questions! ---
#     # Modify these questions to match your data
#     question1 = "How many units of the item with part number 13402939 APTKOREA are in stock at the MTR branch?"
#     answer1 = qa_chain.invoke(question1)
#     print(f"\n❓ Question: {question1}")
#     print(f"✅ Answer: {answer1['result']}")

#     question2 = "What is the total sale quantity for the FRONT RH SHOCK ABSORBER?"
#     answer2 = qa_chain.invoke(question2)
#     print(f"\n❓ Question: {question2}")
#     print(f"✅ Answer: {answer2['result']}")

#     question3 = "What is the stock quantity for the item with part number 96473229 APTKOREA at the MTR branch?"
#     answer3 = qa_chain.invoke(question3)
#     print(f"\n❓ Question: {question3}")
#     print(f"✅ Answer: {answer3['result']}")

#     question4 = "What is the total sale quantity for the BRAKE SHOE AVEO REAR  200-2014?"
#     answer4 = qa_chain.invoke(question4)
#     print(f"\n❓ Question: {question4}")
#     print(f"✅ Answer: {answer4['result']}")

#     question5 = "What is the overall sale percentage for the item named BRAKE SHOE AVEO REAR  200-2014?"
#     answer5 = qa_chain.invoke(question5)
#     print(f"\n❓ Question: {question5}")
#     print(f"✅ Answer: {answer5['result']}")

#     question6 = "How many units of the item with part number 58302-H6A00 APTKOREA have been sold (SSALE)"
#     answer6 = qa_chain.invoke(question6)
#     print(f"\n❓ Question: {question6}")
#     print(f"✅ Answer: {answer6['result']}")

#     question7 = "What is the brand of the item named BRAKE SHOE AVEO REAR  200-2014?"
#     answer7 = qa_chain.invoke(question7)
#     print(f"\n❓ Question: {question7}")
#     print(f"✅ Answer: {answer7['result']}")

#     question8 = "Tell me the balance quantity for the item with part number 58302-H6A00 APTKOREA"
#     answer8 = qa_chain.invoke(question8)
#     print(f"\n❓ Question: {question8}")
#     print(f"✅ Answer: {answer8['result']}")