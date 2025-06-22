import sys

from openai import OpenAI
client = OpenAI()

def summarize_code(file_name):
    print(f"Summary of {file_name}:")
    with open(file_name, 'r') as code_file:
        code = code_file.read()
        prompt = f"Summarize the following code:\n ```{code}```"
        ##print(f"prompt = {prompt}")
        response = client.responses.create(
            model = 'gpt-4.1',
            input = prompt
        )
        print("Parakeet says:")
        print(response.output_text)

def convert_code_java(file_name):
    print(f'Convert code to Java: {file_name}')
    with open(file_name, 'r') as code_file:
        code = code_file.read()
        prompt = f"Convert the following code into Java:\n ```{code}```"
        ##print(f"prompt = {prompt}")
        response = client.responses.create(
            model = 'gpt-4.1',
            input = prompt
        )
        print("Parakeet says:")
        print(response.output_text)

def convert_code_csharp(file_name):
    print(f'Convert code to C#: {file_name}')

def convert_code_python(file_name):
    print(f'Convert code to Python: {file_name}')


def suggest_unit_tests(file_name):
    print(f'Suggest unit tests: {file_name}')


print("parakeet v0.1: for fun and learning.")
if len(sys.argv) < 3:
    print("Need at least 2 parameters: parakeet [command] [input]")
    sys.exit(1)

theCommand = sys.argv[1]
theFile = sys.argv[2]
if theCommand == 'summarize':
    summarize_code(theFile)
elif theCommand == 'covert-java':
    convert_code_java(theFile)
elif theCommand == 'unit-tests':
    suggest_unit_tests(theFile)