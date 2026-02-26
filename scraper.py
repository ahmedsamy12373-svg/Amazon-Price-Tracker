import pandas as pd

# محاكاة سحب بيانات أسعار الموبايلات
data = [
    {'Product': 'iPhone 15', 'Price': 45000, 'Store': 'Amazon'},
    {'Product': 'Samsung S23', 'Price': 35000, 'Store': 'Amazon'},
    {'Product': 'Realme 11', 'Price': 12000, 'Store': 'Amazon'}
]

df = pd.DataFrame(data)
# حساب السعر بعد الضريبة كمرحلة Transformation
df['Price_With_Tax'] = df['Price'] * 1.14

print("ETL Process: Data Extracted and Transformed Successfully.")
print(df)
