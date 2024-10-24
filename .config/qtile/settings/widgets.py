import subprocess
from libqtile import widget, bar
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

widget_defaults = {
    'foreground': colors['inactive'],
    'font': 'JetBrains Mono',
    'fontsize': 13,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()

def separatorInvisible():
    return widget.Sep(
            linewidth=0,
            padding=13,
            #background = "ffffff",
            )

def icon(fontsize=13, text="?", padding=0):
    return widget.TextBox(
        fontsize=fontsize,
        text=text,
        foreground=colors['inactive'],
        padding=padding,
    )

def workspaces(): 
    return [
        widget.GroupBox(
            font='JetBrains Mono',
            fontsize=13,
            margin_y=3,
            margin_x=0,
            padding_y=3,
            padding_x=3,
            borderwidth=1,
            active=colors['urgent'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='line',
            highlight_color = colors['inactive'],
            block_highlight_text_color = colors['color1'],
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['color1'],
            this_screen_border=colors['inactive'],
            other_current_screen_border=colors['inactive'],
            other_screen_border=colors['inactive'],
            disable_drag=True,
            center_aligned=True
        ),
    ]

def get_volume_icon():
    try:
       
        volume = int(subprocess.check_output("pamixer --get-volume", shell=True).strip())
        mute = subprocess.check_output("pamixer --get-mute", shell=True).decode("utf-8").strip()
        
        # Casos:
        #1. si esta mute mostrar simbolo y el porcentaje.
        #2. si no esta mute mostrar icono y porcentaje normal, mostrar por separado.
        if mute == "true":
            return f"󰸈{volume}%"

        # Determina el icono basado en el nivel de volumen
        elif volume < 30:
            return ""
        elif volume < 70:
            return ""
        elif volume >= 70:
            return ""
    except:
        return ""  # En caso de error

def get_volume():
    try:
       
        volume = int(subprocess.check_output("pamixer --get-volume", shell=True).strip())
        
        return f"{volume}%"
    
    except:
        return ""  # En caso de error


def get_battery_status():
    try:
        # Comando que obtiene el porcentaje de la batería
        battery_percentage = subprocess.check_output(
            "acpi | grep -P -o '[0-9]+(?=%)'", shell=True).decode("utf-8").strip()
        
        # Comando que verifica si está enchufada o no
        battery_state = subprocess.check_output(
            "acpi -a", shell=True).decode("utf-8").strip()
        
        if 'on-line' in battery_state:
            #󱐌
            #return f"{battery_percentage}%"
            return ""
        elif 'off-line' in battery_state:
            if int(battery_percentage) >= 80:
                return "󱊣"
            elif int(battery_percentage) > 50:
                return "󱊢"
            elif int(battery_percentage) >= 20:
                return "󱊡"
            elif int(battery_percentage) < 20:
                return "󰂃"
    except Exception as e:
        return "󰂑N/A"

primary_widgets = [

    # Clock
    icon(text="󱇼 ", fontsize=18),
    #  , 󱇼 , 󰣇 
    widget.Clock(format='%A, %d %b/%y %H:%M'),

    separatorInvisible(),
        
    # Prompt
    widget.Prompt(),

    separatorInvisible(),
        
    # Spacer dinamic
    widget.Spacer(length=bar.STRETCH),

    # Workspaces
    *workspaces(),

    # Spacer dinamic
    widget.Spacer(length=bar.STRETCH),
    
    # Updates
    #icon(text="󰚰"),
    #widget.CheckUpdates(
    #     colour_have_updates=colors['color3'],
    #     colour_no_updates=colors['inactive'],
    #     no_update_string='0',
    #     display_format='{updates}',
    #     update_interval=1800,
    #     distro='Arch_checkupdates',
    #     custom_command='checkupdates',
    #),
    # 
    #separatorInvisible(),
    #
    ## Battery
    ## Icono dinamico del nivel de la bateria
    #widget.GenPollText(
    #        padding = -3,
        #    func=get_battery_status,  
        #update_interval=0.3, # sec
        #),
#
#    widget.Battery(
#        format="{percent:2.0%}",
#        low_percentage=0.30,
##        low_foreground=colors['urgent'],
#        notify_below=30,
#        update_interval=13, # sec
#    ),
#
#    separatorInvisible(),
#
    # Temps  
#    icon(text="", padding = -1),
#    widget.ThermalSensor(
#          padding = 0,
#          threshold=50,
#          tag_sensor="Core 0",
#    ),
#
#    # Lo comento porque consume demasiados recursos del sistema 
#    # por la actualizacion que debe hacer a cada momento y repetidamente
#    #icon(text="", padding = 1),
    #widget.ThermalSensor(
#    #         padding = 0,
#    #         threshold=50,
#    soc_dts1-virtual-0 and temp number.
#    #         tag_sensor="soc_dts1-1",
#    #),
#
##    #separatorInvisible(),
#
#    # Volume
#    # Icono dinamico del nivel del volumen 
#    # Lo comento porque consume demasiados recursos del sistema 
#    # por la actualizacion que debe hacer a cada momento y repetidamente
    #widget.GenPollText(
        #func=get_volume_icon,
        #update_interval=0.2,  
        #width = 15,
    #),
    
    # Porcentaje dinamico del nivel del volumen 
    #widget.GenPollText(
        #func=get_volume,
        #update_interval=0.1,  
        #width = 33,
    #),

    #separatorInvisible(),

    # Net
#    icon(text="󰓅"),
#    widget.Net(padding=0, width=55, format='{down:7.2f}', interface='wlp2s0', use_bits = False),
#    widget.Net(padding=0, width=15, format='{down_suffix}', interface='wlp2s0', use_bits = False),
#    icon(text=""),
#    widget.Net(padding=0, width=55, format='{up:7.2f}', interface='wlp2s0', use_bits = False),
#    widget.Net(padding=0, width=15, format='{up_suffix}', interface='wlp2s0', use_bits = False),
#    icon(text=""),
#
    # System
    widget.Systray(),

    # Layouts
    widget.CurrentLayoutIcon(scale=0.65),
    #widget.CurrentLayout(padding=1),
]

secondary_widgets=[
    # Here configure widgets for your second monitor or the others
    separatorInvisible()
]

