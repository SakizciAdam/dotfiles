import subprocess
result = str(subprocess.check_output(['acpi', '-b']))
charging=result.count('Discharging')<=0
percentage=int(result.split(",")[1].replace(" ","").replace("\n","").replace("\\n","").replace("\'","").replace("%",""))
if not charging:
    if percentage<10:
        print('󰁺',end='')
    elif percentage<20:
        print('󰁻',end='')
    elif percentage<30:
        print('󰁼',end='')
    elif percentage<40:
        print('󰁽',end='')
    elif percentage<50:
        print('󰁾',end='')
    elif percentage<60:
        print('󰁿',end='')
    elif percentage<70:
        print('󰁾',end='')
    elif percentage<80:
        print('󰂁',end='')
    elif percentage<90:
        print('󰂂',end='')
    else:
        print('󱟢',end='')
else:
    print('󰂄',end='')
print(''+str(percentage)+"%",end='\n')