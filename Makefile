save:
	@echo "Executing the save of the file in the database"
	python3 save2.py $$FILE_NAME $$MONGO_URI
	@echo "The file is now saved"

python_installs:
	pip install dnspython