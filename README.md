# Sentiment and Text Analysis CLI

A simple command-line tool to perform sentiment analysis, classification, or summarization on text reviews using the `mall` library and an Ollama LLM.
This tool was developed for a project to analyze marketing data from a customer survey. Customers responded to questions using free-format text, hence the need for a language-model approach.

## Prerequisites

- Python 3.8 or higher
- [mall](https://pypi.org/project/mall/) package
- [polars](https://pypi.org/project/polars/) package
- [Ollama](https://ollama.com/) installed and configured
- Pull your desired model, e.g.:

```bash
    ollama pull llama3.2
```

## Installation

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install mall polars
```

Ensure Ollama is available in your PATH.

## Usage

```bash
./script.py <input.txt> <output.csv> <action> [options]
```

- `<input.txt>`: Path to a text file where each non-empty line is a review.
- `<output.csv>`: CSV file where results will be written.
- `<action>`: One of:
  - `sentiment`: Perform sentiment analysis (labels: positive, neutral, negative)
  - `classify`: Classify into custom labels (requires `--labels`)
  - `summarize`: Summarize text (uses `--length`)

### Options

--engine: LLM engine (default: ollama)

--model: Model name (default: llama3)

--seed: Random seed (default: 100)

--labels: Space-separated list of labels for classification

--length: Number of sentences for summarization (default: 7)

### Examples

#### Sentiment Analysis

```bash
./script.py reviews.txt output.csv sentiment
```

#### Classification

```bash
./script.py reviews.txt classified.csv classify --labels expense time-consuming skills
```

#### Summarization

```bash
./script.py reviews.txt summary.csv summarize --length 5
```

## Error Handling

The script will exit with an error message if:

The input file is missing or empty

An invalid action is provided

Required options (e.g., --labels for classify) are missing

LLM configuration or analysis fails
