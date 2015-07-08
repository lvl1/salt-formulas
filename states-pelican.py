import salt.exceptions
import subprocess

def build_site(name, output="/srv/www"):
    # /srv/salt/_states/pelican.py
    # Generates static site with pelican -o $output $name
    # Sorry.
    # -- Jadon Bennett, 2015

    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}

    # I don't know how to make this work. But it's cool.
    #current_state = __salt__['pelican.current_state'](name)
    current_state = "cool"

    if __opts__['test'] == True:
        ret['comment'] = 'Markdown files from "{0}" will be converted to HTML and put in "{1}"'.format(name,output)
        ret['changes'] = {
            'old': current_state,
            'new': 'New!',
        }
        ret['result'] = None

        return ret

    subprocess.call(['pelican', '-o', output, name])

    ret['comment'] = 'Static site generated from "{0}".'.format(name)

    ret['changes'] = {
        'old': current_state,
        'new': 'Whoopee!',
    }

    ret['result'] = True

    return ret
