import pandas as pd
import time
import random

file = "task3.csv"   # 👈 apna CSV naam daal

while True:
    df = pd.read_csv(file, encoding='latin-1')

    # existing columns print kar (first time check ke liye)
    print(df.columns)

    # new row create (adjust based on your columns)
    new_row = {}

    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower():
            new_row[col] = pd.Timestamp.now()
        elif df[col].dtype == 'int64' or df[col].dtype == 'float64':
            new_row[col] = random.randint(50, 500)
        else:
            new_row[col] = "Updated"

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_csv(file, index=False)

    print("New row added 🔥")

    time.sleep(5)