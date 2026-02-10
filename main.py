import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("there is no api key found")

client = genai.Client(api_key=api_key)




parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='Chatbot',
                    epilog='Text at the bottom of help')
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")


args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]




#response = client.models.generate_content(model='gemini-2.5-flash',contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
#response = client.models.generate_content(model='gemini-2.5-flash',contents=args.user_prompt)
response = client.models.generate_content(model='gemini-2.5-flash',contents=messages)


if response.usage_metadata.prompt_token_count is not None:
    prompt_token_count = response.usage_metadata.prompt_token_count
if response.usage_metadata.candidates_token_count is not None:
    candidates_token_count = response.usage_metadata.candidates_token_count
if args.verbose :
    print(f"User prompt: {args.user_prompt}\nPrompt tokens: {prompt_token_count}\nResponse tokens: {candidates_token_count}\n{response.text}")
else:
    print(response.text)





def main():
    #print("Hello from ai-agent!")
    pass


if __name__ == "__main__":
    main()
