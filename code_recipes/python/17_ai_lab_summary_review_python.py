import pandas as pd

from src.sample_data import AI_LITERACY_SUMMARY_REVIEW_CASES
from src.ai_review import make_review_summary, review_ai_summaries

cases = pd.read_csv(AI_LITERACY_SUMMARY_REVIEW_CASES)
reviewed = review_ai_summaries(cases)
summary = make_review_summary(reviewed)

print(summary)
print(reviewed[["case_id", "notebook_topic", "review_status", "risky_claim_categories"]])
