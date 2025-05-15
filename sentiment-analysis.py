import sys
import argparse
import mall
import polars as pl


def load_reviews(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            raise ValueError("Input file is empty or contains only blank lines.")
        return pl.DataFrame({"review": lines})
    except FileNotFoundError:
        sys.exit(f"Error: File not found: {path}")
    except Exception as e:
        sys.exit(f"Error reading {path}: {e}")


def analyze(df, action, column, options):
    # Configure the model
    try:
        engine, model = options.engine, options.model
        df.llm.use(engine, model, options=dict(seed=options.seed))
    except Exception as e:
        sys.exit(f"Error configuring LLM: {e}")

    # Perform requested analysis
    try:
        if action == "sentiment":
            return df.llm.sentiment(column)
        elif action == "classify":
            if not options.labels:
                sys.exit("Error: --labels is required for classification.")
            return df.llm.classify(column, options.labels)
        elif action == "summarize":
            return df.llm.summarize(column, options.length)
        else:
            sys.exit(f"Unknown action '{action}'. Choose from sentiment, classify, summarize.")
    except Exception as e:
        sys.exit(f"Error during {action}: {e}")


def write_output(df, out_path):
    try:
        df.write_csv(out_path)
        print(f"Results written to {out_path}")
    except Exception as e:
        sys.exit(f"Error writing output: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Perform LLM-driven analysis on a text file of reviews."
    )
    parser.add_argument("input", help="Path to input .txt file")
    parser.add_argument("output", help="Path to output CSV file")
    parser.add_argument(
        "action",
        choices=["sentiment", "classify", "summarize"],
        help="Type of analysis to perform",
    )
    parser.add_argument(
        "--engine", default="ollama",
        help="LLM engine (default: ollama)"
    )
    parser.add_argument(
        "--model", default="llama3",
        help="LLM model name (default: llama3)"
    )
    parser.add_argument(
        "--seed", type=int, default=100,
        help="Random seed for reproducibility (default: 100)"
    )
    parser.add_argument(
        "--labels", nargs='+',
        help="Labels for classification (required for classify action)"
    )
    parser.add_argument(
        "--length", type=int, default=7,
        help="Number of sentences for summarization (default: 7)"
    )

    args = parser.parse_args()

    df = load_reviews(args.input)
    result = analyze(df, args.action, "review", args)
    print(result)
    write_output(result, args.output)


if __name__ == "__main__":
    main()