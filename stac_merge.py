import json
import logging
import os
import sys

from unity_sds_client.resources.dataset import Dataset
from unity_sds_client.resources.data_file import DataFile

# stage_in packages
from unity_sds_client.resources.collection import Collection

if len(sys.argv) < 2:
    print("stac_merge requires at least 2 arguments:")
    print("stac_merge.py output_dir stac_file1 ... <stac_filen>")
    sys.exit(0)
    
# inputs
#"/unity/ads/input_collections/SBG-L2-RSRFL/catalog.json", "/unity/ads/input_collections/SBG-L1B-PRE/catalog.json"]
stac_files = sys.argv[2:]

#"/unity/ads/input_collections/REFLECT_CORRECT_MERGE"
output_location = sys.argv[1]

if len(stac_files) == 0:
    print("Not enough stac files given, nothing to do")
    sys.exit()
    
master_collection = Collection.from_stac(stac_files[0])

for file in stac_files[1:]:
  temp_collection = Collection.from_stac(file)
  for ds in temp_collection.datasets:
    master_collection.add_dataset(ds)

Collection.to_stac(master_collection, output_location)
