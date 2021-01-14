

ssh-git:
	ssh-keyscan github.com >> ~/.ssh/known_hosts

install-zsh:
	cd .. && sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
