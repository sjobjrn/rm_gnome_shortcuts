import subprocess

print("WARNING!")
yes_no = input("This will remove all keyboard shortcuts from gnome (Y/N)")
if yes_no == 'Y':

    proc1 = subprocess.Popen("gsettings list-recursively org.gnome.settings-daemon.plugins.media-keys", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    k1 = list(proc1.stdout)

    proc2 = subprocess.Popen("gsettings list-recursively org.gnome.desktop.wm.keybindings", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    k2 = list(proc2.stdout)

    proc3 = subprocess.Popen("gsettings list-recursively org.gnome.shell.keybindings", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    k3 = list(proc3.stdout)

    keys_list = k1 + k2 + k3
    for line in keys_list[1:]:
        line_splitd = line.split(" ", 2)
        shortcut = line_splitd[0] + " " + line_splitd[1]
        print("gsettings set {} ['']".format(shortcut))
    #"gsettings set {} [''].format(shortcut)"