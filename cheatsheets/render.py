from os import path
import sys

import jinja2
import markdown
import weasyprint

def get_template(template_name):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

    return env.get_template(template_name)


BASE_URL = path.abspath(path.dirname(__file__))

if __name__ == '__main__':
    markdown_filename = sys.argv[1]
    with open(markdown_filename) as f:
        raw_markdown = f.read()

    filename_noext, _ = path.splitext(markdown_filename)
    pdf_filename = '%s.pdf' % filename_noext
    html_filename = '%s.html' % filename_noext

    print('Converting markdown to HTML...')
    html = markdown.markdown(raw_markdown, output='html5')
    print('Done.')

    template = get_template('template.html')

    print('Rendering template...')
    rendered = template.render({
        'html': html,
    })
    print('Done.')

    print('Writing HTML file...')
    with open(html_filename, 'w+') as f:
        f.write(rendered)
    print('Done.')

    print('Converting to PDF...')
    weasyprint.HTML(string=rendered, base_url=BASE_URL).write_pdf(pdf_filename)
    print('Done.')

