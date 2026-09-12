# Evaluation script for blog-engine
import os

def evaluate():
    workspace = os.environ.get('WORKSPACE_PATH', '.')
    # Check for required output files
    required_files = ['blog_config.json']
    for file in required_files:
        if not os.path.exists(os.path.join(workspace, file)):
            return False
    return True
