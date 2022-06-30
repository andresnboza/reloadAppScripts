temp:
	@echo "\n### Executing the save of the file in the database ###\n"
	npm run save
	@echo "\n### The file is now saved ###\n"

save:
	@echo "Executing the save of the file in the database"
	mongofiles -d media put "ReadmeAppService1.md"
	@echo "The file is now saved"

install_mongosh_linux:
	@echo "START - Installation of mongosh"
	wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
	@echo "END - Installation of mongosh"

install_mongosh_linux_if_error:
	@echo "START - Installation of mongosh IF ERROR"
	sudo apt-get install gnupg
	wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
	echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
	sudo apt-get update
	sudo apt-get install -y mongodb-mongosh
	@echo "END - Installation of mongosh IF ERROR"

server:
	cd server && npm start

python_installs:
	pip install dnspython