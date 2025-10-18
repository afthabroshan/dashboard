# import os
# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient
# import traceback

# print("--- Starting Hugging Face Connection Test ---")

# # 1. Load the .env file
# load_dotenv()

# # 3. Verify that the token was loaded
# if hf_token:
#     # Print a confirmation without showing the whole key
#     print(f"✅ Token loaded successfully! Starts with: '{hf_token[:5]}...'")
# else:
#     print("❌ FATAL: Token not found in environment.")
#     print("--> Please check your .env file. Is it named correctly? Does it contain HUGGINGFACEHUB_API_TOKEN=...?")
#     exit()

# # 4. Attempt a direct API call
# try:
#     print("\n⏳ Attempting a direct call to the Hugging Face API...")
#     client = InferenceClient(token=hf_token)
#     response = client.chat.completions.create(
#     model="inclusionAI/Ling-1T",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the capital of France?"
#         }
#     ],
# )

#     print("✅ SUCCESS: Direct API call worked!")
#     print("Response:", response)

# except Exception as e:
#     print(f"❌ FATAL: Direct API call failed.")
#     print("--> This confirms the problem is with your API token or network connection.")
#     print(f"--> Error type: {type(e).__name__}")
#     print(f"--> Error message: {e}")
#     print("\nFull traceback:")
#     traceback.print_exc()

# print("\n--- Test Complete ---")


# # import requests
# # requests.get("https://huggingface.co")