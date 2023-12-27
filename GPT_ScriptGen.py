```python
import openai
import json
from security import secure_data

class GPT_ScriptGen:
    def __init__(self, api_key):
        self.api_key = api_key
        self.gpt = openai.GPT(api_key=self.api_key)

    def get_user_input(self):
        script_type = input("Enter the type of script you want to generate: ")
        script_purpose = input("Enter the purpose of the script: ")
        script_parameters = input("Enter the parameters for the script: ")
        return script_type, script_purpose, script_parameters

    def generate_script(self, script_type, script_purpose, script_parameters):
        prompt = f"Generate a {script_type} Python script for {script_purpose} with parameters {script_parameters}"
        response = self.gpt.submit_request(prompt)
        if response.is_ok:
            return response.choices[0].text.strip()
        else:
            return "Error in generating script. Please try again."

    def customize_script(self, script):
        variables = input("Enter the variables you want to use in the script: ")
        function_names = input("Enter the function names you want to use in the script: ")
        customized_script = script.replace("variable", variables).replace("function", function_names)
        return customized_script

    def save_script(self, script):
        with open("generated_script.py", "w") as file:
            file.write(script)

    def run(self):
        script_type, script_purpose, script_parameters = self.get_user_input()
        generated_script = self.generate_script(script_type, script_purpose, script_parameters)
        customized_script = self.customize_script(generated_script)
        self.save_script(customized_script)

if __name__ == "__main__":
    api_key = secure_data("api_key")
    script_gen = GPT_ScriptGen(api_key)
    script_gen.run()
```
