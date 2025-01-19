# /// script
# requires-python = ">=3.13"
# dependencies = ["pyyaml"]
# ///


import yaml

parts = []
with open('paratext.txt', 'r', encoding='UTF-8') as f:
    parts = yaml.safe_load(f)


def handle_item(chunk):
    out = ['<div class="item">']
    for parts in chunk['cons']:
        cons = parts['cons']
        mytype = parts['type']
        if isinstance(cons, list):
            out.append(handle_item({'cons': cons}))
        else:
            if mytype == 'img':
                out.append(f"<img src='{cons}'/>")
            else:
                out.append(f"<p>{cons}</p>")   
    out.append('</div>')
    return '\n'.join(out)

def weave(chunk):
    out = ['<div class="container">']
    out.append(handle_item(chunk))
    out.append('</div>')
    return '\n'.join(out)


def main():
    for chunk in parts:
        print(weave(chunk))
 
if __name__ == "__main__":
    main()
