import os, argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt

def main():
    load_dotenv()
    api_key=os.environ.get('OPENAI_API_KEY')
    if api_key is None:
        raise RuntimeError(
            'OPENAI_API_KEY not found.'
        )

    client = OpenAI(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument('user_prompt', type=str, help='User prompt')
    parser.add_argument('--verbose', action='store_true', help='enable verbose output')
    args = parser.parse_args()

    messages = []
    messages.append({'role': 'system', 'content': system_prompt})
    messages.append({'role': 'user', 'content': args.user_prompt})

    response = client.responses.create(
        model='gpt-4.1-mini',
        input=messages
    )
    
    if response.usage is None:
        raise RuntimeError(
            'prompt failed, check your internet or api_key'
        )

    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {response.usage.input_tokens}')
        print(f'Response tokens: {response.usage.output_tokens}')

    print(response.output_text)

if __name__ == "__main__":
    main()
