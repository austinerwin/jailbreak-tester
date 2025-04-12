# Jailbreak Tester

A tool for testing jailbreak prompts against language models to ensure they properly reject harmful content.

## Setup

1. Clone this repository
2. Create a `.env` file with your OpenRouter API key (copy from `.env.example`)
3. Install requirements: `pip install -r requirements.txt`

## Usage

### Input Files

1. `models.txt` - Comma-separated list of OpenRouter models to test (e.g., `openai/gpt-4o-mini, anthropic/claude-3-haiku`)
2. `/jailbreaks` directory - Each .txt file contains a jailbreak prompt that will be used as the system message
3. `/messages` directory - Each .txt file contains a test message that would typically be rejected

### Running Tests

```bash
python jailbreak_tester.py
```

To use a different model for verification:

```bash
python jailbreak_tester.py
```

### Output

The program will:
1. Display progress in the console as each test runs
2. Show a summary of results for each jailbreak and model
3. Display detailed line-by-line test results
4. Generate a timestamped log file with complete test details

## How It Works

The tester:
1. Tests each model against each jailbreak with each message
2. Uses a verification model to determine if the response is a refusal or an acceptance
3. Logs successes (jailbreak worked) and failures (model refused despite jailbreak)

## Example Files

The repository includes sample jailbreaks, messages, and model configurations to get started.
