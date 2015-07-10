import salt.exceptions

def build_site(name, output="/srv/www"):
    # /srv/salt/_states/pelican.py
    # Generates static site with pelican -o $output $name
    # Sorry.
    # -- Jadon Bennett, 2015

    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}

    current_state = __salt__['pelican.current_state'](name)

    if __opts__['test'] == True:
        ret['comment'] = 'Markdown files from "{0}" will be converted to HTML and put in "{1}"'.format(name,output)
        ret['changes'] = {
            'old': current_state,
            'new': 'New!',
        }
        ret['result'] = None

        return ret

    new_state = __salt__['pelican.generate'](output,name)

    ret['comment'] = 'Static site generated from "{0}".'.format(name)

    ret['changes'] = {
        'old': current_state,
        'new': new_state,
    }

    ret['result'] = True

    return ret
