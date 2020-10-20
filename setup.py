#!/usr/bin/env python3
import sys
from shutil import which
import platform
import subprocess
import os


def exists(name):
    return which(name) is not None


def install(name):
    proc = subprocess.Popen("sudo apt install -y " + name, shell=True)
    try:
        outs, errs = proc.communicate(timeout=15)
    except TimeoutError:
        proc.kill()
        exit("Failed to install " + name)
    proc.wait()


platform = platform.system()
homedir = os.getenv("HOME")
os.chdir(homedir)
if not exists("brew") and platform == "Darwin":
    xcode = subprocess.Popen("xcode-select --install", shell=True, stdin=None)
    xcode.wait()
    brew = subprocess.Popen(
        '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',
        shell=True, stdin=None)
    brew.wait()
if not exists("git"):
    if platform == "Linux":
        install("git")
if not exists("zsh"):
    if platform == "Linux":
        install("zsh")
    elif platform == "FreeBSD":
        zsh = subprocess.Popen("sudo pkg install zsh", shell=True, stdin=None)
        zsh.wait()
    elif platform == "Darwin":
        zsh = subprocess.Popen("brew install zsh", shell=True, stdin=None)
        zsh.wait()
if not exists("tmux"):
    if platform == "Linux":
        install("tmux")
    elif platform == "FreeBSD":
        tmux = subprocess.Popen("sudo pkg install tmux", shell=True, stdin=None)
        tmux.wait()
    elif platform == "Darwin":
        tmux = subprocess.Popen("brew install tmux", shell=True, stdin=None)
        tmux.wait()
if not exists("starship"):
    if platform == "FreeBSD":
        starship = subprocess.Popen("sudo pkg install starship", shell=True, stdin=None)
        starship.wait()
    else:
        starship = subprocess.Popen("curl -fsSL https://starship.rs/install.sh | bash", shell=True, stdin=None)
        starship.wait()

chsh = subprocess.Popen("chsh -s $(which zsh)", shell=True, stdin=None)
chsh.wait()
installOmz = subprocess.Popen(
    "sh -c \"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"", shell=True,
    stdin=None)
installOmz.wait()
zshAutosuggestions = subprocess.Popen("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions",
                              shell=True,
                              stdin=None)
zshAutosuggestions.wait()
zshHighlighting = subprocess.Popen("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting",
                              shell=True,
                              stdin=None)
zshHighlighting.wait()
installTpm = subprocess.Popen("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm",
                              shell=True,
                              stdin=None)
installTpm.wait()


try:
    os.remove(homedir + "/.zshrc")
except OSError:
    pass
try:
    os.remove(homedir + "/.tmux.conf")
except OSError:
    pass
try:
    os.symlink(homedir + "/dotfiles/zshrc", homedir + "/.zshrc")
except (FileNotFoundError, FileExistsError):
    print("Cannot create zshrc symlink\n", sys.exc_info()[0])
    print("UID: ", os.getuid())
try:
    os.symlink(homedir + "/dotfiles/tmux.conf", homedir + "/.tmux.conf")
except (FileNotFoundError, FileExistsError):
    print("Cannot create tmux-conf symlink\n", sys.exc_info()[0])
    print("UID: ", os.getuid())
