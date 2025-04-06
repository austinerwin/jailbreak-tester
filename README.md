# LLM Jailbreak Effectiveness Tester

This Python program evaluates the effectiveness of jailbreak prompts against Large Language Models (LLMs) using OpenRouter. It tests whether an LLM responds to a message when given a jailbreak prompt (pass) or refuses (fail).

## Features
- Tests jailbreak prompts against various OpenRouter LLMs.
- Determines if the jailbreak successfully bypasses content restrictions.

## Setup
### Clone the Repository
Clone this repository to your local machine:

```bash
git clone [your-repo-link-here]
cd [your-repo-name-here]
```

Replace `[your-repo-link-here]` and `[your-repo-name-here]` with your actual GitHub repository link and directory name.

### Install Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

### OpenRouter API Key
1. Create an API key at [OpenRouter](https://openrouter.ai).
2. Create a `.env` file in your project root directory and insert your API key:

```
OPENROUTER_API_KEY=your-api-key-here
```

You can create the `.env` file from the command line by making sure you're in the root directory and running:
  ```bash
  echo "OPENROUTER_API_KEY=your-api-key-here" > .env
  ```

Replace `your-api-key-here` with your actual OpenRouter API key.

## Running the Program
Ensure:
- Input files are correctly populated and located in the `inputs` directory.
- Dependencies are installed.

Then, execute the script with:

- Windows:
  ```bash
  python jailbreak_tester.py
  ```

- Linux/Mac:
  ```bash
  python3 jailbreak_tester.py
  ```

## Input Files
Ensure the following input files exist and are properly formatted. The program will raise an error if these files do not exist:

- **`inputs/models.txt`**
  - Contains a comma-separated list of OpenRouter model identifiers.
  - Example:
    ```
    openai/gpt-4o-mini,google/gemini-pro
    ```

- **`inputs/jailbreaks.csv`**
  - CSV file containing jailbreak prompts (one jailbreak per row).

- **`inputs/messages.csv`**
  - CSV file containing messages to test against jailbreak prompts (one message per row).

## Troubleshooting
- Ensure `.env` file is correctly named and formatted.
- Verify your API key from OpenRouter is valid.
- Confirm input files exist and have proper formatting.
