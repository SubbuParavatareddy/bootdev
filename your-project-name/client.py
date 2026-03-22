from google import genai

# Only run this block for Gemini Developer API
client = genai.Client(api_key='AIzaSyBYXs2tvBUSrJWSiUlCwkcsK8eWnSPZdmk')
print(client)