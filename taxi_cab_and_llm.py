import duckdb
import boto3
import openai
import pandas as pd

# 1. Load Parquet from public S3 into DuckDB or pd.DataFrame
con = duckdb.connect()
con.execute("""
  SELECT trip_distance, fare_amount, passenger_count
  FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2019-01.parquet')
  LIMIT 1000
""")
df = con.fetchdf()

# 2. Prepare few-shot prompt with CSV snippet
sample_csv = df.sample(50).to_csv(index=False)
prompt = f"""
You are a smart data analyst. Clean this data snippet:
- Drop rows where passenger_count is zero,
- Compute avg trip_distance and avg fare,
and output a clean summary table.

Data:
{sample_csv}
"""

resp = openai.ChatCompletion.create(model="gpt-4", messages=[{"role":"user","content":prompt}])
cleaned_summary = resp.choices[0].message.content

# 3. Save summary back to S3
s3 = boto3.client('s3')
s3.put_object(Bucket='your-bucket', Key='curated/summary.txt', Body=cleaned_summary)

# 4. Question phase
qa_prompt = f"Summary:\n{cleaned_summary}\n\nQuestion: What is the average fare?"
resp2 = openai.ChatCompletion.create(model="gpt-4", messages=[{"role":"user","content":qa_prompt}])
print(resp2.choices[0].message.content)
