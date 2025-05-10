from pymongo import MongoClient
import pandas as pd

# Database setup and connection
client = MongoClient("mongodb+srv://tengstc03:gnZkqiGDUmg0EgLE@cluster0.qj4ohkg.mongodb.net/?tls=true")
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