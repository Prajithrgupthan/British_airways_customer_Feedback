import pandas as pd

df = pd.read_csv('BA_reviews.csv')

num_lines = len(df)

#total user reviews taken
print("Number of lines:", num_lines)

#Verified Travel list
trip_verified_count = len(df[df['reviews'].str.contains('Trip Verified')])
print("'Trip Verified' count:", trip_verified_count)
trip_notverified_count = len(df[df['reviews'].str.contains('Not Verified')])
print("'Trip Verified' count:", trip_notverified_count)


# Combine multiple columns into a single string
combined_text = df.astype(str).apply(lambda x: ' '.join(x), axis=1)

# Check for the presence of 'positive' or 'positives' and count the occurrences
delay_count = combined_text.str.contains(r'\bdelay\b', case=False).sum()
delays_count = combined_text.str.contains(r'\bdelays\b', case=False).sum()

# Compute the total count
total_count = delay_count + delays_count

# Print the result
print("Total count of 'delay' or 'delays':", total_count)






