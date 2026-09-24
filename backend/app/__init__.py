import os
import sys

# Ensure repository root is on sys.path so 'backend.app' is always resolvable
_current_dir = os.path.dirname(os.path.abspath(__file__))  # .../backend/app
_backend_dir = os.path.dirname(_current_dir)               # .../backend
_repo_root = os.path.dirname(_backend_dir)                 # .../skillexa-app

for path in [_repo_root, _backend_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)
