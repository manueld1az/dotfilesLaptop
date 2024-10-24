# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from libqtile.config import Match
from .theme import colors

# Layouts and layout rules


layout_conf_withBorder = {
    'border_focus': colors['inactive'][0],
    'border_normal': colors['dark'][0],
    'border_width': 3,
    'margin': 10,
}

layout_conf_withoutBorder = {
    'border_focus': colors['inactive'][0],
    'border_normal': colors['dark'][0],
    'border_width': 0,
    'margin': 0,
}

layouts = [
    layout.Max(**layout_conf_withoutBorder),
    #layout.MonadTall(**layout_conf),
    #layout.MonadWide(**layout_conf),
    #layout.Bsp(**layout_conf),
    #layout.Matrix(columns=2, **layout_conf),
    #layout.RatioTile(**layout_conf),
    layout.Columns(**layout_conf_withBorder),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color1"][0]
)
