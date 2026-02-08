import pandas as pd
import sys
import numpy as np
import time

class90 = pd.read_csv("E:\\MSc\\HPC\\2024\\USalign\\USalign_data_final_class90_merged_torppa_blosum_scores_LENGTH_NORMALIZED.csv")
print(class90.dtypes)

start = time.time()

for i, row1 in class90.iterrows():

    aligned_length = class90.at[i, 'Aligned_length']

    # ACTUALLY PERFORM NORMALIZATION BASED ON ALIGNED LENGTH
    class90.at[i, 'Torppa90_lengthNorm_score'] = (class90.at[i, 'Torppa90_Score']) / (aligned_length)
    class90.at[i, 'Torppa60_lengthNorm_score'] = (class90.at[i, 'Torppa60_Score']) / (aligned_length)
    class90.at[i, 'Blosum90_lengthNorm_score'] = (class90.at[i, 'Blosum90_Score']) / (aligned_length)
    class90.at[i, 'Blosum62_lengthNorm_score'] = (class90.at[i, 'Blosum62_Score']) / (aligned_length)

end = time.time()

print("Length-based normalization of existing base scores took ", (end-start), " seconds") 

class90.to_csv("E:\\MSc\\HPC\\2024\\USalign\\October25\\USalign_data_final_class90_merged_torppa_blosum_scores_LENGTH_NORMALIZED_fix1_October25.csv")
class90 = pd.read_csv("E:\\MSc\\HPC\\2024\\USalign\\October25\\USalign_data_final_class90_merged_torppa_blosum_scores_LENGTH_NORMALIZED_fix1_October25.csv")

start2 = time.time()

# Find the maximal and minimal length-normalized scores
T90_lengthNorm_min_score = class90['Torppa90_lengthNorm_score'].min()
T90_lengthNorm_max_score = class90['Torppa90_lengthNorm_score'].max()

T60_lengthNorm_min_score = class90['Torppa60_lengthNorm_score'].min()
T60_lengthNorm_max_score = class90['Torppa60_lengthNorm_score'].max()

B90_lengthNorm_min_score = class90['Blosum90_lengthNorm_score'].min()
B90_lengthNorm_max_score = class90['Blosum90_lengthNorm_score'].max()

B62_lengthNorm_min_score = class90['Blosum62_lengthNorm_score'].min()
B62_lengthNorm_max_score = class90['Blosum62_lengthNorm_score'].max()

end2 = time.time()

print("Finding min's and max's took ", (end2-start2), " seconds")

start3 = time.time()

# Get the relative normalized scores to facilitate comparison between matrices
for i, row1 in class90.iterrows():
    class90.at[i, 'Torppa90_relative_lengthNorm_score'] = (class90.at[i, 'Torppa90_lengthNorm_score'] - T90_lengthNorm_min_score) / (T90_lengthNorm_max_score - T90_lengthNorm_min_score)
    class90.at[i, 'Torppa60_relative_lengthNorm_score'] = (class90.at[i, 'Torppa60_lengthNorm_score'] - T60_lengthNorm_min_score) / (T60_lengthNorm_max_score - T60_lengthNorm_min_score)
    class90.at[i, 'Blosum90_relative_lengthNorm_score'] = (class90.at[i, 'Blosum90_lengthNorm_score'] - B90_lengthNorm_min_score) / (B90_lengthNorm_max_score - B90_lengthNorm_min_score)
    class90.at[i, 'Blosum62_relative_lengthNorm_score'] = (class90.at[i, 'Blosum62_lengthNorm_score'] - B62_lengthNorm_min_score) / (B62_lengthNorm_max_score - B62_lengthNorm_min_score)

end3 = time.time()

print("Calculating relative lengthNorm scores took ", (end3-start3), " seconds")
class90.to_csv("E:\\MSc\\HPC\\2024\\USalign\\October25\\USalign_data_final_class90_merged_torppa_blosum_scores_LENGTH_NORMALIZED_fix1_October25.csv")
