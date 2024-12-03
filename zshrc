export PATH=~/go/bin:$PATH
export PATH=$HOME/dotfiles:$PATH
export PATH=$HOME/bin:$PATH
export PATH=/usr/local/sbin:$PATH

export ZDOTDIR=$HOME/.config/zsh
export HOMEBREW_GITHUB_API_TOKEN=
export ZSH=$HOME/.oh-my-zsh
export LC_ALL=en_US.UTF-8

plugins=(
  git
  golang
  z
  zsh-autosuggestions
  zsh-syntax-highlighting
  kubectl
  aws
  brew
  fzf
  jira
  kubetail
  terraform
)

source $ZSH/oh-my-zsh.sh
zstyle ':completion:*' special-dirs true

if [[ "$TMUX" == "" ]] && [[ "$SSH_CONNECTION" != "" ]]; then
  WHOAMI=$(whoami)
  if tmux has-session 2>/dev/null; then
    tmux a
  else
    tmux
  fi
fi

if type brew &>/dev/null; then
    FPATH=$(brew --prefix)/share/zsh-completions:$FPATH
 
    autoload -Uz compinit
    compinit
 fi
 
source <(kubectl completion zsh)

eval "source <("/opt/homebrew/bin/starship" init zsh --print-full-init)"

HISTFILE=~/.zsh_history
HISTSIZE=100000
SAVEHIST=100000
setopt SHARE_HISTORY 
