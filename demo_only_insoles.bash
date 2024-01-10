#!/usr/bin/env bash
SESSION_NAME=demo

source "`rospack find tmux_session_core`/common_functions.bash"
ros_core_tmux "$SESSION_NAME"

tmux set -g pane-border-status top

W1=(
"roslaunch moticon_insoles read_sdk.launch --wait"
"rqt_plot"
"roslaunch republisher republisher_insoles.launch --wait"
"roslaunch moticon_insoles show_urdf.launch ignore_insole_imu_for_vis:=false"
)

create_tmux_window "$SESSION_NAME" "main_nodes" "${W1[@]}"

tmux -2 a -t $SESSION_NAME
