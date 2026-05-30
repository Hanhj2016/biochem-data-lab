import pandas as pd

from src.ai_review import make_review_summary, review_ai_summaries

cases = pd.read_csv("data/ai_literacy/ai_lab_summary_review_cases.csv")
reviewed = review_ai_summaries(cases)
summary = make_review_summary(reviewed)

print(summary)
print(reviewed[["case_id", "notebook_topic", "review_status", "risky_claim_categories"]])
