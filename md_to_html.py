import argparse
import markdown

parser = argparse.ArgumentParser(description='Convert a markdown file to HTML.')

parser.add_argument('input_file', help='The input markdown file.')
parser.add_argument('output_file', help='The output HTML file.')

args = parser.parse_args()

with open(args.input_file, 'r') as file:
    md_text = file.read()

html = markdown.markdown(md_text)

with open(args.output_file, 'w') as file:
    file.write(html)
