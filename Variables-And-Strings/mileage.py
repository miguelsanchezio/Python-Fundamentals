KMS_IN_MILE = 1.60934

print('How many kilometers did you run today?')
kms = float(input())
miles = round(kms/KMS_IN_MILE, 2)

print(f'Awesome! You ran {miles} miles.')