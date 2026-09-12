# Evaluation script for activity-logger
import os

def evaluate():
    workspace = os.environ.get('WORKSPACE_PATH', '.')
    # Check for required output files
    required_files = ['activity_log.csv']
    for file in required_files:
        if not os.path.exists(os.path.join(workspace, file)):
            return False
    return True
