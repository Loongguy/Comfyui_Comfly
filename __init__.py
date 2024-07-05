from .AiHelper import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, WEB_DIRECTORY


__all__ = ['AiHelper','WEB_DIRECTORY', 'NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']


def start_ai_helper():
    import threading
    import subprocess
    import os
    import sys
    import aiohttp


    def run_ai_helper():
        ai_helper_path = os.path.join(os.path.dirname(__file__), "AiHelper.py")
        subprocess.run([sys.executable, ai_helper_path])

    ai_helper_thread = threading.Thread(target=run_ai_helper)
    ai_helper_thread.start()


start_ai_helper()

