save: python_installs save2

save2:
	@echo "Executing the save of the file in the database"
	python3 save2.py $$FILE_NAME $$MONGO_URI
	@echo "The file is now saved"

copy:
	@echo "START - Copy file"
	python3 copy.py $$FILE_NAME
	@echo "END - Copy file"

update:
	git add .
	git commit -m "update on the scripts"
	git push

python_installs:
	pip install dnspython
	pip install bson