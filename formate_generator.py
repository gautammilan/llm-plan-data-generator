# import argparse
import json
import os
def apply_chat_template(example):
    """
    Transform the prompt and completion of an example into a specified format.
    """
    formatted_text = f'<s>[INST] <<SYS>>\\n\\n<</SYS>>\\n\\n{example["prompt"]} [/INST] {example["completion"]} </s>'
    # Update the example with the new formatted text
    new_text = {"text": formatted_text}
    return new_text

def main(args):
    # Create the parser
    # parser = argparse.ArgumentParser(description='Apply chat template to given JSON input.')

    # Add an argument for the example JSON
    # parser.add_argument('--x_file', type=str, help='The JSON string representing the example. It must have "prompt" and "completion" fields.')

    # parser.add_argument('--y_file', type=str, help='The JSON string representing the example. It must have "prompt" and "completion" fields.')
    # parser.add_argument('--output_file', type=str, help='The JSON string representing the example. It must have "prompt" and "completion" fields.')


    # Parse the example JSON string
    try:
        with open(args["x_file"], "r") as f:
            x_data = json.load(f)
        with open(args["y_file"],"r") as f:
            y_data= json.load(f)
    except json.JSONDecodeError:
  
        print(f"Error: The provided example is not a valid JSON string.{os.path.isfile(args.x_file)}\
              {os.path.isfile(args.y_file)}")
        return
    print("file succesfully loaded")
    # Validate the example structure
    # Apply the chat template
    with open("test_formatted.jsonl", "w") as f:

        for i in range(len(x_data)):
            result = apply_chat_template({"prompt":x_data[str(i)],"completion":y_data[str(i)]})
            f.write(json.dumps(result)+"\n")

argument= {"x_file":"llm-plan-data-generator/x_data_test.json", "y_file":"llm-plan-data-generator/y_data_test.json","output_file":"test_formatted.jsonl"}
main(argument)
