
import subprocess


def get_state():
    a = str(subprocess.run(['ip','link'], stdout=subprocess.PIPE).stdout)

    for x in a.splitlines():
        x=x.replace('\\n','\n')
        if x.count('state UP')>0:
            return '󰖟'
        
    return '󱞐'

    
print(get_state(),'')

