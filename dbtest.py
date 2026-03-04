import os
from dotenv import load_dotenv 
from pymongo import MongoClient
import pandas as pd

load_dotenv()

# Database setup and connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["smartbin"]

# Collections
dustbin_col = db["dustbins"]
notification_col = db["notification"]
collect_rubbish_col = db["collectRubbish"]
user_account_col = db["userAccount"]
rubbish_col = db["rubbish"]

sample = dustbin_col.find_one()
# print(sample)

# sample_df = pd.DataFrame(sample, index=[0])
dustbin_df = pd.DataFrame(list(dustbin_col.find()))
print(dustbin_df)