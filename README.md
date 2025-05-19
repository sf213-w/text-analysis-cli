# Sentiment and Text Analysis CLI

This repository provides two command-line tools built with the `mall` library and an Ollama LLM for analyzing free-form customer responses. These scripts support sentiment analysis, custom classification, summarization, and applying custom prompts. This tool was developed for a project to analyze marketing data from a customer survey. Customers responded to questions using free-format text, hence the need for a language-model approach.

## Prerequisites

* Python 3.8 or higher
* [mall](https://pypi.org/project/mall/)
* [polars](https://pypi.org/project/polars/)
* [Ollama](https://ollama.com/) installed and configured
* Pull your desired model, e.g.:

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
pip install mlverse-mall
pip install polars
```

Ensure Ollama is available in your `PATH`.

---

## Script 1: `sentiment-analysis.py`

### Usage of Script 1

```bash
python sentiment-analysis.py <input.txt> <output.csv> <action> [options]
```

* `<input.txt>`: Path to a text file where each non-empty line is a review.
* `<output.csv>`: CSV file where results will be written.
* `<action>`: One of:

  * `sentiment`: Perform sentiment analysis (labels: positive, neutral, negative)
  * `classify`: Classify into custom labels (requires `--labels`)
  * `summarize`: Summarize text (uses `--length`)

### Options

* `--engine`: LLM engine (default: `ollama`)
* `--model`: Model name (default: `llama3`)
* `--seed`: Random seed (default: `100`)
* `--labels`: Space-separated list of labels for classification
* `--length`: Number of sentences for summarization (default: `7`)

### Examples

#### Sentiment Analysis

```bash
python sentiment-analysis.py reviews.txt sentiment.csv sentiment
```

#### Classification

```bash
python sentiment-analysis.py reviews.txt classify.csv classify --labels fast expensive helpful
```

#### Summarization

```bash
python sentiment-analysis.py reviews.txt summary.csv summarize --length 5
```

---

## Script 2: `custom-prompt.py`

This script allows you to apply a custom prompt to each line of a text file.

### Usage of Script 2

```bash
python custom-prompt.py <input.txt> <prompt.txt> [--output output.csv] [--engine ollama] [--model llama3.2] [--seed 100]
```

* `<input.txt>`: Path to the input file (one entry per line)
* `<prompt.txt>`: Path to a `.txt` file containing your custom prompt
* `--output`: (Optional) Path to write CSV output
* `--engine`: LLM engine to use (default: `ollama`)
* `--model`: LLM model name (default: `llama3.2`)
* `--seed`: Random seed for reproducibility (default: `100`)

### Example

#### Apply Prompt

Given a prompt file like:

```
For each entry determine if the customer is happy. Answer only yes or no.
```

Run:

```bash
python custom-prompt.py reviews.txt prompt.txt --output result.csv
```

---

## Error Handling

Both scripts will exit with a clear error message if:

* The input or prompt file is missing or empty
* Required options are not provided
* An invalid action is used
* LLM configuration fails
