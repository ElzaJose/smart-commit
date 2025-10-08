# Smart Commit CLI

## Overview

Smart Commit CLI is a Python script designed to help teams standardize their git commit messages. By generating commit messages in a specific, agreed-upon format, this tool ensures that all contributors follow the same conventions, making commit history more readable and understandable for everyone involved in the project.

## Features
- Prompts users to enter commit details in a structured way
- Generates commit messages in a consistent, project-specific format
- Helps maintain a clean and informative git history
- Reduces ambiguity and improves collaboration

## Why Use Smart Commit CLI?
- **Consistency:** Enforces a standard commit message format across the team
- **Clarity:** Makes it easier to understand the purpose of each commit
- **Best Practices:** Encourages descriptive and meaningful commit messages

## Usage

1. **Install Requirements**
	 - Make sure you have Python 3 installed.
     - Clone this repo and install the utility globally as a Python package using pip:
        ```bash
        pip install -e .
        ``` 

2. **Run the Script**
	- If installed globally, you can run the command directly as `smart-commit`
		```bash
		smart-commit
		```
	- Follow the prompts to enter your commit details.
	- The script will generate a commit message in the required format.

3. **Input Data**
    - `Ticket number` : Enter the ticket number associated with your changes
    - `Short Description` : Give a brief summary for your change 
    - `Reason for Change` : Give the reason in detail on why you have done the changes
    - `Type` : Select one of the options given or give your custom input 
    - `Scope` : Select one of the options given or give your custom input

4. **Preview**

![smart-commit Preview](Preview/Preview.gif)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License.
