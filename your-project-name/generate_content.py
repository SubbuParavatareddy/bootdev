from client import client
response = client.models.generate_content(
    model='gemini-2.5-flash', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
)
if response.usage_metadata is not None: 
    print(f"Prompt Token : {response.usage_metadata.prompt_token_count}")
    print(f"Response Token : {response.usage_metadata.candidates_token_count}")    
    print(response.text)