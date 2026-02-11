import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from functions.call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("there is no api key found")

client = genai.Client(api_key=api_key)




parser = argparse.ArgumentParser(
                    prog='Ai Agent',
                    description='Ai Coding Agent powered by Gemini')
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")


args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]




#response = client.models.generate_content(model='gemini-2.5-flash',contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
#response = client.models.generate_content(model='gemini-2.5-flash',contents=args.user_prompt)
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt),)

        #temperature=0

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    if response.usage_metadata.prompt_token_count is not None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    if response.usage_metadata.candidates_token_count is not None:
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# Handle function calls or text response
if response.function_calls:
    function_results = []

    for function_call in response.function_calls:
        # Call the function and get the result
        function_call_result = call_function(function_call, verbose=args.verbose)

        # Validate the result
        if not function_call_result.parts:
            raise Exception("Function call result has no parts")

        if function_call_result.parts[0].function_response is None:
            raise Exception("Function call result has no function_response")

        if function_call_result.parts[0].function_response.response is None:
            raise Exception("Function call result has no response")

        # Print result if verbose
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_results.append(function_call_result.parts[0])
else:
    print(response.text)



"""
if response.usage_metadata.prompt_token_count is not None:
    prompt_token_count = response.usage_metadata.prompt_token_count
if response.usage_metadata.candidates_token_count is not None:
    candidates_token_count = response.usage_metadata.candidates_token_count
#if args.verbose :
#    print(f"User prompt: {args.user_prompt}\nPrompt tokens: {prompt_token_count}\nResponse tokens: {candidates_token_count}\n{response.text}")
#else:
#    print(response.text)


# Handle function calls or text response
if response.function_calls:
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
else:
    print(response.text)
"""



def main():
    #print("Hello from ai-agent!")
    pass


if __name__ == "__main__":
    main()
