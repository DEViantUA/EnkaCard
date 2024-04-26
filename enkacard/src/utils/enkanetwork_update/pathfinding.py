import sys
import os

async def search():
    python_paths = sys.path

    enkanetwork_path = None

    for path in python_paths:
        enkanetwork_candidate = os.path.join(path, "enkanetwork")
        if os.path.exists(enkanetwork_candidate):
            enkanetwork_path = enkanetwork_candidate
            break

    if enkanetwork_path:
        assets_path = os.path.join(enkanetwork_path, "assets")

        if not os.path.exists(assets_path):
            os.makedirs(assets_path)
            
        return assets_path
