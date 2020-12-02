import logging

loger = logging.getLogger(__name__)
loger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test.log")
formatter = logging.Formatter('%(asctime)s   ::   %(message)s  :: %(name)s')
file_handler.setFormatter(formatter)

loger.addHandler(file_handler)

loger.info("Salam Mirlan")
