# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
#ZSH_THEME="lambda-mod"
ZSH_THEME="avit"


# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git extract cp zsh-autosuggestions zsh-syntax-highlighting)


if [[ $TERM == "dumb" ]]; then	# in emacs
    PS1='%(?..[%?])%!:%~%# '
    # for tramp to not hang, need the following. cf:
    # http://www.emacswiki.org/emacs/TrampMode
    unsetopt zle
    unsetopt prompt_cr
    unsetopt prompt_subst
    unfunction precmd
    unfunction preexec
else
    source $ZSH/oh-my-zsh.sh
fi

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

if [ -d ~/.texmf ] ; then
    export TEXMFHOME=~/.texmf
fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"
find .ssh/ -mindepth 1 -maxdepth 1 -name 'id_ed25519*' ! -name '*.pub' -print0 | xargs -0 ssh-add 2>/dev/null

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

alias v="vim"
alias md="mkdir"
alias gtree='git log --oneline --decorate --all --graph'
alias fw='sudo /etc/init.d/iptables'

alias settings='gnome-control-center'
alias startvpn='sudo openvpn openvpn-science.ovpn'
alias startwork='ssh sandor'
alias skype='skypeforlinux'
alias skype2='skypeforlinux --secondary'

alias rzsh='source ~/.zshrc'

alias -s py='python3'
alias -s c='atom'
alias -s h='atom'
alias -s cpp='atom'
alias -s txt='atom'
alias -s md='atom'
alias -s xml='atom'
alias -s v='coqide'
alias -s pdf='evince'

# alias commit='git commit -am "$(curl -s whatthecommit.com/index.txt)"'

vstmake () { rm $1 ; make -C ~/Documents/VST $PWD/$1 ; }

export PATH=~/bin:$PATH:/bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:/usr/local/sbin
#export PATH=$PATH:/home/biv/Documents/Personnal/eclipse/bin/x86_64_linux
export PATH=~/Documents/fstar/bin:$PATH

alias svn=~/.dotfiles/bin/svn-color.py
export GTK_IM_MODULE=xim

# OPAM configuration
. /home/biv/.opam/opam-init/init.zsh > /dev/null 2> /dev/null || true
