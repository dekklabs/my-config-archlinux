# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from theme.color import Color

from os import path
import subprocess

# colores
color = Color()


@hook.subscribe.startup_once
def autostart():
    subprocess.call(
        [path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])


mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Programas
    # Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Browser
    Key([mod], "b", lazy.spawn("firefox")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "s", lazy.spawn("/usr/bin/google-chrome-stable")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Gestor de archivos visual
    Key([mod], "e", lazy.spawn("thunar")),


    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in [" ", " ", " ", " ", " ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    'border_focus': '#F07178',
    'border_width': 1,
    'margin': 3
}

layouts = [
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font='UbuntuMono Nerd Font',
    font='UbuntuMono Nerd Font',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=18,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    this_current_screen_border=color.secondary(),
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=color.secondary(),
                    other_screen_border=color.primary(),
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground=color.secondary(),
                    background=["#0f101a", "#0f101a"],
                    fontsize=12,
                    font='UbuntuMono Nerd Font Bold',
                ),
                # Imagen arrow 1
                widget.Image(
                    filename=path.join(path.expanduser(
                        '~'), '.config', 'qtile', 'img', '2bar.png'),
                ),
                # Icono de cambio de tipo de pantalla
                widget.CurrentLayoutIcon(
                    foreground=["#0f101a", "#0f101a"],
                    background=color.secondary(),
                    scale=0.65
                ),
                # Cambio de tipo de pantalla
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=color.secondary()
                ),
                # Imagen arrow 2
                widget.Image(
                    filename=path.join(path.expanduser(
                        '~'), '.config', 'qtile', 'img', '1bar.png')
                ),
                # widget.Chord(
                #     chords_colors={
                #         'launch': ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # Icono de relog
                widget.TextBox(
                    background=color.primary(),
                    foreground=["#0f101a", "#0f101a"],
                    text='',
                    padding=10
                ),
                # Fecha y hora
                widget.Clock(
                    background=color.primary(),
                    foreground=["#0f101a", "#0f101a"],
                    format='%d/%m/%Y - %H:%M ',
                ),
                # Imagen arrow 1
                widget.Image(
                    filename=path.join(path.expanduser(
                        '~'), '.config', 'qtile', 'img', '3bar.png'),
                ),
                # Lista de Programas
                widget.Systray(),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=["#0f101a", "#0f101a"],
                ),
            ],
            24,
            opacity=0.95
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=18,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    this_current_screen_border=color.secondary(),
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=["#a151d3", "#a151d3"],
                    other_screen_border=["#a151d3", "#a151d3"],
                    disable_drag=True
                ),
                widget.WindowName(
                    foreground=color.secondary(),
                    background=["#0f101a", "#0f101a"],
                    fontsize=12,
                    font='UbuntuMono Nerd Font Bold',
                ),
                widget.Image(
                    filename=path.join(path.expanduser(
                        '~'), '.config', 'qtile', 'img', '2bar.png'),
                ),
                widget.CurrentLayoutIcon(
                    foreground=["#0f101a", "#0f101a"],
                    background=color.secondary(),
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=color.secondary()
                ),
                widget.Image(
                    filename=path.join(path.expanduser(
                        '~'), '.config', 'qtile', 'img', '1bar.png'),
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.Sep(
                #     linewidth=0,
                #     padding=5,
                #     background=color.secondary()
                # ),
                widget.TextBox(
                    background=color.primary(),
                    foreground=["#0f101a", "#0f101a"],
                    text='',
                    padding=10
                ),
                widget.Clock(
                    background=color.primary(),
                    foreground=["#0f101a", "#0f101a"],
                    format='%d/%m/%Y - %H:%M '
                ),
                # Imagen arrow 1
                widget.Image(
                    filename=path.join(path.expanduser(
                        '~'), '.config', 'qtile', 'img', '3bar.png'),
                ),
            ],
            24,
            opacity=0.95
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], border_focus='#a15d13')
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
