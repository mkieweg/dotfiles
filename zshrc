export PATH=~/go/bin:$PATH
export PATH=$HOME/dotfiles:$PATH
export PATH=/usr/local/sbin:$PATH

export ZDOTDIR=$HOME/.config/zsh
export HOMEBREW_GITHUB_API_TOKEN=
export ZSH=$HOME/.oh-my-zsh

plugins=(
  git
  golang
  z
  zsh-autosuggestions
  zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh
zstyle ':completion:*' special-dirs true

eval "source <("/usr/local/bin/starship" init zsh --print-full-init)"