#!/usr/bin/env bash

# This file is part of The RetroPie Project
#
# The RetroPie Project is the legal property of its developers, whose names are
# too numerous to list here. Please refer to the COPYRIGHT.md file distributed with this source.
#
# See the LICENSE.md file at the top-level directory of this distribution and
# at https://raw.githubusercontent.com/RetroPie/RetroPie-Setup/master/LICENSE.md
#

rp_module_id="retropie-music"
rp_module_desc="RetroPie Menu Background Music"
rp_module_help="placeholder"
rp_module_licence="placeholder"
rp_module_section="exp"
rp_module_flags="noinstclean nobin"

function depends_retropie-music() {
  local depends=(python3)
  getDepends "${depends[@]}"
}

function sources_retropie-music() {
  gitPullOrClone "$md_inst" "https://github.com/OfficialPhilcomm/retropie-music.git" master
}

function install_retropie-music() {
  cd "$md_inst"
  chown -R $user:$user "$md_inst"
  sudo ./install.sh
}

function enable_retropie-music() {
  sudo service enable retropie_background_music
  printMsgs "dialog" "retropie-music enabled. It will start automatically on next boot"
}

function disable_retropie-music() {
  sudo service disable retropie_background_music
  printMsgs "dialog" "retropie-music disabled. It will no longer start automatically on boot"
}

function remove_retropie-music() {
  printMsgs "dialog" "todo"
}

function gui_retropie-music() {
  local cmd=()
  local options=(
    1 "Start retropie-music now"
    2 "Stop retropie-music now"
    3 "Enable retropie-music on Boot"
    4 "Disable retropie-music on Boot"
  )
  local choice
  local error_msg
  
  while true; do
    cmd=(dialog --backtitle "$__backtitle" --menu "\n\nChoose an option." 22 86 16)
    choice=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
    
    if [[ -n "$choice" ]]; then
      case "$choice" in
        1)
          sudo service retropie_background_music start
          ;;

        2)
          sudo service retropie_background_music stop
          ;;

        3)  
          enable_retropie-manager
          ;;

        4)
          disable_retropie-manager
          ;;
      esac
    else
      break
    fi
  done
}
