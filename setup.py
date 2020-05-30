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
        exit("Failed ti install " + name)
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
        zsh = subprocess.Popen(sudo pkg install zsh, shell=True, stdin=None)
        zsh.wait()
    elif platform == "Darwin":
        zsh = subprocess.Popen("brew install zsh", shell=True, stdin=None)
        zsh.wait()
if not exists("tmux"):
    if platform == "Linux":
        install("tmux")
    elif platform == "FreeBSD":
        tmux = subprocess.Popen(sudo pkg install tmux, shell=True, stdin=None)
        tmux.wait()
    elif platform == "Darwin":
        tmux = subprocess.Popen("brew install tmux", shell=True, stdin=None)
        tmux.wait()

chsh = subprocess.Popen("chsh -s $(which zsh)", shell=True, stdin=None)
chsh.wait()
installOmz = subprocess.Popen(
    "sh -c \"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"", shell=True,
    stdin=None)
installOmz.wait()
tmuxThemes = subprocess.Popen("git clone https://github.com/boisjacques/tmux-themepack.git ~/.tmux-themepack",
                              shell=True,
                              stdin=None)
tmuxThemes.wait()
fonts = subprocess.Popen("git clone https://github.com/boisjacques/fonts.git", shell=True, stdin=None)
fonts.wait()
fontInstall = subprocess.Popen("fonts/install.sh", shell=True, stdin=None)
fontInstall.wait()
os.remove(homedir + "/.zshrc")
os.remove(homedir + "/.tmux.conf)
try:
    if platform == "Linux":
        os.symlink(homedir + "/dotfiles/linux-zshrc", homedir + "/.zshrc")
    if platform == "Darwin":
        os.symlink(homedir + "/dotfiles/macos-zshrc", homedir + "/.zshrc")
except (FileNotFoundError, FileExistsError):
    print("Cannot create zshrc symlink\n", sys.exc_info()[0])
    print("UID: ", os.getuid())
try:
    os.symlink(homedir + "/dotfiles/tmux.conf", homedir + "/.tmux.conf")
except (FileNotFoundError, FileExistsError):
    print("Cannot create tmux-conf symlink\n", sys.exc_info()[0])
    print("UID: ", os.getuid())
