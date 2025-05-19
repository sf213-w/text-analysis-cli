import pandas as pd

# Load the Excel file
df = pd.read_excel("HIPAA-Challenges-Responses-June-2020.xlsx")

# Extract column D by position (0-based index, so D is index 3)
column_d = df.iloc[:, 3].dropna()

# Write to a text file, one line per cell
with open("responses2020.txt", "w", encoding="utf-8") as f:
	for line in column_d:
		cleaned = str(line).replace("\n", " ").replace("\r", " ").strip()
		if cleaned:  # Skip if the result is still empty
			f.write(cleaned + "\n")
