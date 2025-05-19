import polars as pl
import mall

# Load the CSV file
df = pl.read_csv("output.csv")

# Filter for sentiment
positive_df = df.filter(pl.col("sentiment") == "negative")

# Use the LLM to summarize why the reviews are positive
positive_df.llm.use("ollama", "llama3.2", options=dict(seed=100))
summary_df = positive_df.llm.summarize("review")  # 5 sentences, adjust as needed

# Display or save the result
print(summary_df)
summary_df.write_csv("negative_summary.csv")
