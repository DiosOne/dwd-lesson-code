diary_file = "diary_entry.txt"

# 1. Write two lines about your day (use 'w' mode)
with open(diary_file,'w') as f:
    f.write("It's too early for brain work\n" )
    f.write("I need more coffee I think\n")

# 2. Read and print content (use 'r' mode)
with open(diary_file,'r') as f:
    
