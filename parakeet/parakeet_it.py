import sys

## constants
MODEL_VERSION = 'gpt-4.1'
PARAKEET_SAYS = 'Parakeet says:'

from openai import OpenAI
client = OpenAI()

def summarize_code(file_name):
    print(f"Summary of {file_name}:")
    with open(file_name, 'r') as code_file:
        code = code_file.read()
        prompt = f"Summarize the following code:\n ```{code}```"
        ##print(f"prompt = {prompt}")
        response = client.responses.create(
            model = MODEL_VERSION,
            input = prompt
        )
        print(PARAKEET_SAYS)
        print(response.output_text)


def convert_code_helper(file_name, new_language_pretty):
    print(f'Convert code to {new_language_pretty}: {file_name}')
    with open(file_name, 'r') as code_file:
        code = code_file.read()
        prompt = f"Convert the following code into {new_language_pretty}:\n ```{code}```"
        ##print(f"prompt = {prompt}")
        response = client.responses.create(
            model = MODEL_VERSION,
            input = prompt
        )
        print(PARAKEET_SAYS)
        print(response.output_text)



def suggest_unit_tests(file_name):
    print(f'Suggest unit tests: {file_name}')
    with open(file_name, 'r') as code_file:
        code = code_file.read()
        prompt = f"Suggest unit tests for the following code:\n ```{code}```"
        response = client.responses.create(
            model = MODEL_VERSION,
            input = prompt
        )
        print(PARAKEET_SAYS)
        print(response.output_text)


print("parakeet v0.1: For fun and learning.")
if len(sys.argv) < 3:
    print("Need at least 2 parameters: parakeet [command] [input]")
    sys.exit(1)

theCommand = sys.argv[1]
theFile = sys.argv[2]
if theCommand == 'summarize':
    summarize_code(theFile)
elif theCommand == 'convert-java':
    convert_code_helper(theFile, 'Java')
elif theCommand == 'convert-csharp':
    convert_code_helper(theFile, 'C#')
elif theCommand == 'convert-python':
    convert_code_helper(theFile, 'Python')
elif theCommand == 'unit-tests':
    suggest_unit_tests(theFile)
else:
    print(f"Unknown command: {theCommand}")
    sys.exit(1)