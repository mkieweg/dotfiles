export PATH=~/go/bin:$PATH
export PATH=$HOME/dotfiles:$PATH
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
)

source $ZSH/oh-my-zsh.sh
zstyle ':completion:*' special-dirs true

if [[ "$TMUX" == "" ]] && [[ "$SSH_CONNECTION" != "" ]]; then
  WHOAMI=$(whoami)
  if tmux has-session 2>/dev/null; then
    tmux a
  else
    $HOME/dotfiles/tmuxgo
  fi
fi

eval "source <("/usr/local/bin/starship" init zsh --print-full-init)"