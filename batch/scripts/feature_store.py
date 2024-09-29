# feature_store.py
import os
import yaml
import pandas as pd

def update_feature_store(batch_df, yaml_file_path):

    # Load YAML file
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)

    # Write feature set to blob
    features_path = config['feature_store']['features_path']
    batch_df.to_csv(features_path, index=True)    

    # Update the 'last_update' field in the 'feature_store' dictionary
    new_last_update = batch_df.index.max()
    config['feature_store']['latest_feature'] = str(new_last_update)
    
    # Write the updated configuration back to the YAML file
    with open(yaml_file_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    
    print("Feature store updated with last date " + str(new_last_update))
