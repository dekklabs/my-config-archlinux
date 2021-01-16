#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

if [ -f Ssysresources ]; then
    xrbd -merge $sysresources
fi

if [ -f Ssysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

if [ -d /etc/X11/xinit/xinitrc.d ]; then
    for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
        [ -x "Sf" ] && . "$f"
    done
    unset f
fi

setxkbmap -layout latam &
# feh --bg-scale Downloads/bg.png &
feh --bg-scale Desktop/wallpaper/bg2.jpg &
# pulseaudio &
picom &

udiskie -t &

#!/bin/sh
# xrandr --output HDMI-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-2 --off --output DP-1 --mode 1366x768 --pos 1366x0 --rotate normal --output HDMI-3 --off