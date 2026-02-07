# --- THE VIRUS HUNTER SCRIPT ---

# 1. Open the data folder and read the secret virus sequence
with open("data/virus_sample.txt", "r") as file:
    virus_dna = file.read().strip()

print("Successfully loaded virus sequence!")
print("Sequence Length:", len(virus_dna), "bases")

# 2. Search for a specific 'Disease Pattern'
# Let's say 'GCT' is a pattern we are worried about
pattern = "GCT"
if pattern in virus_dna:
    print(f"⚠️ WARNING: Found pattern {pattern} in the virus!")
    print("Pattern count:", virus_dna.count(pattern))
else:
    print(f"✅ CLEAN: Pattern {pattern} not found.")

# 3. Calculate GC Content (Science part)
g_count = virus_dna.count("G")
c_count = virus_dna.count("C")
gc_content = (g_count + c_count) / len(virus_dna) * 100
print(f"GC Stability: {gc_content:.2f}%")
