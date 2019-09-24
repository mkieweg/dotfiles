from shutil import which
import platform
import subprocess
import os


def exists(name):
    return which(name) is not None


platform = platform.system()
os.chdir("~")
if not exists("brew") and platform == "darwin":
    subprocess.run("xcode-select --install")
    subprocess.run('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
if not exists("git"):
    if platform == "linux":
        subprocess.run("sudo apt intall git")
if not exists("zsh"):
    if platform == "linux":
        subprocess.run("sudo apt install zsh")
    elif platform == "darwin":
        subprocess.run("brew install zsh")
    subprocess.run("chsh -s $(which zsh)")
subprocess.run('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
if not exists("tmux"):
    if platform == "linux":
        subprocess.run("sudo apt install tmux")
    elif platform == "darwin":
        subprocess.run("brew install tmux")
subprocess.run("git clone https://github.com/jimeh/tmux-themepack.git ~/.tmux-themepack")
subprocess.run("git clone https://github.com/boisjacques/fonts.git")
subprocess.run("fonts/install.sh")
subprocess.run("git clone https://github.com/boisjacques/tmux-themepack.git")
if platform == "linux":
    os.symlink("~/dotfiles/linux-zshrc", "~/.zshrc")
if platform == "darwin":
    os.symlink("~/dotfiles/macos-zshrc", "~/.zshrc")
os.symlink("~/dotfiles/tmux.conf", "~/.tmux.conf")
