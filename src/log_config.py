import logging

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("C:/Users/www.abcom.in/vscode-workspace/code-repos/selenium-python-test-automation/logs/test_execution.log"),
            logging.StreamHandler()
        ]
    )
    

def get_logger(name):
    return logging.getLogger(name)