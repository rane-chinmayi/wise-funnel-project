import pandas as pd
import numpy as np
import sqlite3


np.random.seed(42)
n_users = 10000

df = pd.DataFrame({
    'user_id': range(1, n_users + 1),
    'signed_up': 1,
    'verified_email': 0,
    'completed_personal_details': 0,
    'submitted_kyc_id': 0,
    'passed_liveness_check': 0,
    'completed_first_transfer_setup': 0,
    'country': np.random.choice(
        ['UK', 'US', 'EU', 'India', 'Other'],
        n_users,
        p=[0.35, 0.25, 0.20, 0.10, 0.10]
    ),
    'device': np.random.choice(
        ['mobile', 'desktop'],
        n_users,
        p=[0.65, 0.35]
    ),
    'account_type': np.random.choice(
        ['personal', 'business'],
        n_users,
        p=[0.75, 0.25]
    )
})

df['verified_email'] = np.random.binomial(1, 0.78, n_users)
df['completed_personal_details'] = df['verified_email'] * np.random.binomial(1, 0.85, n_users)
df['submitted_kyc_id'] = df['completed_personal_details'] * np.random.binomial(1, 0.67, n_users)
df['passed_liveness_check'] = df['submitted_kyc_id'] * np.random.binomial(1, 0.71, n_users)
df['completed_first_transfer_setup'] = df['passed_liveness_check'] * np.random.binomial(1, 0.58, n_users)

df.to_csv('wise_onboarding_funnel.csv', index=False)

conn = sqlite3.connect('wise_funnel.db')
df.to_sql('onboarding', conn, if_exists='replace', index=False)
conn.close()

print(f"Dataset created: {len(df)} users")
print(f"Overall activation rate: {df['completed_first_transfer_setup'].sum() / len(df) * 100:.1f}%")

# Summary CSV for Looker Studio
summary = pd.DataFrame({
    'step': ['Signed Up', 'Verified Email', 'Personal Details', 'KYC Submitted', 'Liveness Check', 'First Transfer'],
    'users': [
        df['signed_up'].sum(),
        df['verified_email'].sum(),
        df['completed_personal_details'].sum(),
        df['submitted_kyc_id'].sum(),
        df['passed_liveness_check'].sum(),
        df['completed_first_transfer_setup'].sum()
    ],
    'dropoff_pct': [0, 21.9, 14.7, 32.9, 29.4, 41.8]
})
summary.to_csv('wise_funnel_summary.csv', index=False)
print("Summary CSV created")

