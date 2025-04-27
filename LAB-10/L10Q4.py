print("Name:Maitrak Barot")
print("Roll no.:24BEE129")
import os
import shutil


source_file = 'source_dir/sample.txt'          
target_dir = 'destination_dir/subfolder'       


os.makedirs(target_dir, exist_ok=True)


destination_file = os.path.join(target_dir, os.path.basename(source_file))


shutil.copy2(source_file, destination_file)

print(f" File copied to: {destination_file}")
