fasta_file = "/home/22042636/Masters/2024/SeqPredNN/Training/PISCES/cullpdb_pc60.0_res0.0-2.2_len40-10000_R0.25_Xray_d2024_01_16_chains26004.fasta"

pdb_ids = []

with open(fasta_file) as f:
    for line in f:
        if line.startswith('>'):
            pdb_id = line[1:5]
            if pdb_id not in pdb_ids:
                pdb_ids.append(pdb_id)
        else:
            continue

unique_ids = set(pdb_ids)

with open("/home/22042636/Masters/2024/SeqPredNN/Training/PDB_id_list.txt", mode="w") as file:
  file.write(", ".join(unique_ids))