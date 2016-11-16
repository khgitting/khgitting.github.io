import os
from subprocess import call
import sys

HOME = os.environ['HOME']
SITE_DIR = os.path.join(HOME, 'github/khgitting.github.io/')
INCLUDES_DIR = os.path.join(SITE_DIR, '_includes/')
POSTS_DIR = os.path.join(SITE_DIR, '_posts/')


def title_and_date_from_filepath(filepath):
    basename = os.path.basename(filepath)
    assert(basename.endswith('.ipynb'))
    date = basename[:10]
    title = basename[11:-6]
    return title, date


def titleize(title):
    return ' '.join(word.capitalize() for word in title.split('-'))
    


def main():
    # add to includes
    filepath = sys.argv[1]
    cmd = ('jupyter nbconvert {} --to html --template full --output-dir {}'
           .format(filepath, INCLUDES_DIR))
    call(cmd.split())

    # add new _posts/ md
    title, date = title_and_date_from_filepath(filepath)
    base = date + '-' + title
    md = base + '.md'
    html = base + '.html'
    lines = []
    # lines.append('---')
    # lines.append('layout: post')
    # lines.append('title: "{}"'.format(titleize(title)))
    # lines.append('date: {}'.format(date))
    # lines.append('---')
    lines.append('')
    lines.append('{{% include {html} %}}'.format(html=html))

    content = '\n'.join(lines)

    with open(os.path.join(POSTS_DIR, md), 'w') as f:
        f.write(content)

    # drop first line ( <!DOCTYPE html> ) from html file
    with open(os.path.join(INCLUDES_DIR, html), 'r') as f:
        lines = f.readlines()[1:]

    with open(os.path.join(INCLUDES_DIR, html), 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    main()
