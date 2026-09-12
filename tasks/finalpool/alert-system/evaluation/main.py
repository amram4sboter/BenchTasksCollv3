# Evaluation script for alert-system
import os

def evaluate():
    workspace = os.environ.get('WORKSPACE_PATH', '.')
    # Check for required output files
    required_files = ['alert_rules.json']
    for file in required_files:
        if not os.path.exists(os.path.join(workspace, file)):
            return False
    return True
