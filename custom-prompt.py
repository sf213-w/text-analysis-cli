# custom_prompt_apply.py

import sys
import argparse
import polars as pl
import mall


def load_text_file(path):
	try:
		with open(path, "r", encoding="utf-8") as f:
			lines = [line.strip() for line in f if line.strip()]
		if not lines:
			raise ValueError("File is empty or contains only blank lines.")
		return lines
	except FileNotFoundError:
		sys.exit(f"Error: File not found: {path}")
	except Exception as e:
		sys.exit(f"Error reading {path}: {e}")


def apply_custom_prompt(data_lines, prompt_text, engine, model, seed):
	try:
		df = pl.DataFrame({"text": data_lines})
		df.llm.use(engine, model, options=dict(seed=seed))
		return df.llm.custom("text", prompt_text)
	except Exception as e:
		sys.exit(f"Error during custom prompt application: {e}")


def main():
	parser = argparse.ArgumentParser(
		description="Apply a custom LLM prompt to each line in a text file."
	)
	parser.add_argument("input", help="Path to input text file")
	parser.add_argument("prompt", help="Path to text file containing custom prompt")
	parser.add_argument(
		"--output", help="Optional output CSV path to write results"
	)
	parser.add_argument(
		"--engine", default="ollama", help="LLM engine to use (default: ollama)"
	)
	parser.add_argument(
		"--model", default="llama3.2", help="LLM model to use (default: llama3)"
	)
	parser.add_argument(
		"--seed", type=int, default=100, help="Random seed (default: 100)"
	)
	

	args = parser.parse_args()

	# Load input and prompt
	input_lines = load_text_file(args.input)
	prompt_lines = load_text_file(args.prompt)
	prompt_text = "\n".join(prompt_lines)

	# Apply prompt
	result_df = apply_custom_prompt(input_lines, prompt_text, args.engine, args.model, args.seed)

	# Show results
	print(result_df)

	# Optionally write to output
	if args.output:
		try:
			result_df.write_csv(args.output)
			print(f"Results written to {args.output}")
		except Exception as e:
			sys.exit(f"Error writing output: {e}")


if __name__ == "__main__":
	main()
