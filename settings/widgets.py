from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(fg='focus'), linewidth=3, padding=5)

def separatorInvisible():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=15, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=50,
        padding=-8
    )


def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='light'),
            font='JetBrainsMono Nerd Font',
            fontsize=15,
            margin_y=3,
            margin_x=0,
            padding_y=3,
            padding_x=3,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='line',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['color5'],
            this_screen_border=colors['focus'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        separatorInvisible(),
        widget.Prompt(),
        widget.WindowName(**base(fg='text'), fontsize=15, padding=5),
        separatorInvisible(),
    ]


primary_widgets = [
    *workspaces(),

    #   Checking Updates
    powerline('color4', 'dark'),
    icon(bg="color4", text=' '),
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['dark'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),


    #   Current Layout tool
    powerline('color3', 'color4'),
    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),
    widget.CurrentLayout(**base(bg='color3'), padding=1),


    #   sensors of system temperature 
    powerline('color2', 'color3'),
    #   CPU icon for cores temperature measurement
    icon(bg="color2", text=''),
    #   CPU0 sensor
    widget.ThermalSensor(
            background=colors['color2'],
            threshold=50,
            tag_sensor="Core 0",
            fmt='{}',
        ),
    #   CPU2 sensor
    widget.ThermalSensor(
            background=colors['color2'],
            threshold=50,
            tag_sensor="Core 2",
            fmt='{}',
        ),

    #   System PC icon and sensor
    #icon(bg='color2', text=''), widget.ThermalSensor(background=colors['color2'], threshold=50, tag_sensor='gigabyte_wmi-6', fmt='{}'),

    #   CPU icon and sensor
    #icon(bg='color2', text=''), widget.ThermalSensor(background=colors['color2'], threshold=50, tag_sensor='Tctl', fmt='{}'),

    #   Grafics icon and sensor
    #icon(bg='color2', text=''), widget.ThermalSensor(background=colors['color2'], threshold=50, tag_sensor='edge', fmt='{}'),


    #   RAM icon and measurement
    powerline('color1', 'color2'),
    icon(bg="color1", text=''),
    widget.Memory(background=colors['color1']),


    #   Speed of connection measurement 
    powerline('grey', 'color1'),
    icon(bg="grey", text='龍 '),
    #   PC wired connection
    #widget.Net(**base(bg='grey'), format='{down}{up}', interface='enp4s0', use_Bytes='true'),
    #   Wi-Fi laptop connection
    widget.Net(**base(bg='grey'), format='{down}{up}', interface='wlp2s0', use_Bytes='true'),


    #   Calendar and Clock
    powerline('dark', 'grey'),
    icon(bg="dark", fontsize=15, text=' '),
    widget.Clock(**base(bg='dark'), format='%d/%m/%Y - %H:%M '),


    #   Systray tool
    powerline('dark', 'dark'),
    widget.Systray(background=colors['dark'], padding=1),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'JetBrainsMono Nerd Font',
    'fontsize': 15,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
