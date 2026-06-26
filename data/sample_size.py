from scipy import stats
import math

# Current KYC submission rate
baseline_rate = 0.671

# Target rate
target_rate = 0.74

# Statistical parameters
alpha = 0.05   # 95% confidence
power = 0.80   # 80% power

# Calculate sample size
z_alpha = stats.norm.ppf(1 - alpha/2)
z_beta = stats.norm.ppf(power)

p_avg = (baseline_rate + target_rate) / 2
n = ((z_alpha + z_beta)**2 * 2 * p_avg * (1 - p_avg)) / (target_rate - baseline_rate)**2

print(f"Required sample size per variant: {math.ceil(n)}")
print(f"Total users needed: {math.ceil(n) * 2}")

# Estimated duration
daily_kyc_starters = 10000 * 0.85 * 0.853
days_needed = (math.ceil(n) * 2) / daily_kyc_starters
print(f"Estimated experiment duration: {math.ceil(days_needed)} days")