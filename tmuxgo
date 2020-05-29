#!/bin/bash
SESSION=`basename $PWD`

tmux -2 new-session -d -s $SESSION

tmux rename-window -t $SESSION:1 vim
tmux split-window   -h
tmux select-pane -t 0
tmux resize-pane -R 30
tmux new-window -t $SESSION -a -n dev
tmux split-window -v
tmux select-pane -t 1
tmux resize-pane -D 15
tmux select-pane -t 0
tmux split-window -h
tmux resize-pane -R 25
tmux select-pane -t 1
tmux split-window -v
tmux new-window -t $SESSION -a -n general-purpose
tmux split-window -h
tmux select-pane -t 0

tmux select-window -t $SESSION:1
tmux -2 attach -t $SESSION
