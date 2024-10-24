# Fix the Java Problem
export _JAVA_AWT_WM_NONREPARENTING=1
export EDITOR=nvim
export VISUAL=nvim

# Enable Powerlevel10k instant prompt. Should stay at the top of ~/.zshrc.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Set up the prompt
autoload -Uz promptinit
promptinit
prompt adam1

setopt histignorealldups sharehistory

# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history

# Use modern completion system
autoload -Uz compinit
compinit

# Comentado para seguridad de redes: zstyle ':completion:*' auto-description 'specify: %d'
# Comentado para seguridad de redes: zstyle ':completion:*' completer _expand _complete _correct _approximate
# Comentado para seguridad de redes: zstyle ':completion:*' format 'Completing %d'
# Comentado para seguridad de redes: zstyle ':completion:*' group-name ''
# Comentado para seguridad de redes: zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
# Comentado para seguridad de redes: zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
# Comentado para seguridad de redes: zstyle ':completion:*' list-colors ''
# Comentado para seguridad de redes: zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
# Comentado para seguridad de redes: zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
# Comentado para seguridad de redes: zstyle ':completion:*' menu select=long
# Comentado para seguridad de redes: zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
# Comentado para seguridad de redes: zstyle ':completion:*' use-compctl false
# Comentado para seguridad de redes: zstyle ':completion:*' verbose true

# Comentado para seguridad de redes: zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
# Comentado para seguridad de redes: zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ -f ~/.p10k.zsh ]] && source ~/.p10k.zsh

# Manual configuration
PATH=/root/.local/bin:/snap/bin:/usr/sandbox/:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/share/games:/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games

# Manual aliases
alias ll='lsd -lh --group-dirs=first'
alias la='lsd -a --group-dirs=first'
alias l='lsd --group-dirs=first'
alias lla='lsd -lha --group-dirs=first'
alias ls='lsd --group-dirs=first'
alias cat='bat'

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# Plugins
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-sudo/sudo.plugin.zsh

# Functions
#function mkt(){
#	mkdir {nmap,content,exploits,scripts}
#}

# Comentado para seguridad de redes: function extractPorts(){
# Comentado para seguridad de redes: 	ports="$(cat $1 | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"
# Comentado para seguridad de redes: 	ip_address="$(cat $1 | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | head -n 1)"
# Comentado para seguridad de redes: 	echo -e "\n[*] Extracting information...\n" > extractPorts.tmp
# Comentado para seguridad de redes: 	echo -e "\t[*] IP Address: $ip_address"  >> extractPorts.tmp
# Comentado para seguridad de redes: 	echo -e "\t[*] Open ports: $ports\n"  >> extractPorts.tmp
# Comentado para seguridad de redes: 	echo $ports | tr -d '\n' | xclip -sel clip
# Comentado para seguridad de redes: 	echo -e "[*] Ports copied to clipboard\n"  >> extractPorts.tmp
# Comentado para seguridad de redes: 	cat extractPorts.tmp; rm extractPorts.tmp
# Comentado para seguridad de redes: }

# Set 'man' colors
function man() {
    env \
    LESS_TERMCAP_mb=$'\e[01;31m' \
    LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    man "$@"
}

# Comentado para seguridad de redes: function rmk(){
# Comentado para seguridad de redes: 	scrub -p dod $1
# Comentado para seguridad de redes: 	shred -zun 10 -v $1
# Comentado para seguridad de redes: }

# Finalize Powerlevel10k instant prompt. Should stay at the bottom of ~/.zshrc.
(( ! ${+functions[p10k-instant-prompt-finalize]} )) || p10k-instant-prompt-finalize

bindkey "^[[H"  beginning-of-line
bindkey "^[[F"  end-of-line

# Binds with Alt_L key 
bindkey "^[[1;3C" end-of-line
bindkey "^[[1;3D" beginning-of-line 

bindkey "^[[3~" delete-char

# Binds with Control_L key
bindkey '^[[1;5C' forward-word
bindkey '^[[1;5D' backward-word

bindkey '^H' backward-kill-word
bindkey '^[[3;5~' kill-word
source /powerlevel10k/powerlevel10k.zsh-theme
