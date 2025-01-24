# /// script
# dependencies = ["markdown2"]
# ///
from abc import ABC, abstractmethod
from pathlib import Path
import markdown2 as md
import re
import sys

class Loom(ABC):
    def __init__(self, head_template="", foot_template=""):
        self.head_template = head_template
        self.foot_template = foot_template

    @abstractmethod
    def merge_as_textfile(self, doc_file, data_file, tag_parser=r'\$[A-Z_\-]\$', parser=None):
         pass
         # read greek document from doc_file containing tags and use tag_parser
         # regex to extract tags from document for content placement

         # if parser is None
         # read data_file with some default simple parser and return a dict of
         # tag -> text chunk 
         # else call parser.parse(data_file_path)

         # replace tags in doc_file with matching text chunk from data_file dict.
         # return the head_template + results of this function + foot_template


    @abstractmethod
    def merge_with_weaver(self, doc_file, data_file, weaver, tag_parser=r'\$[A-Z_\-]\$', parser=None):
        pass
        # Same as above, but has a Weaver class that handles formatting 
        # the info in the data file to a required format

      
class DataParser(ABC):

    @abstractmethod
    def parse(self, data_file_path):
        pass
        # parse data_file to dict of keys -> text chunks
        # this would let people use a simple text file or yaml or json etc.
        # to store the data that will be 


class Weaver(ABC):
    @abstractmethod
    def weave(self, text):
        pass
        # get data from data_dict using chunk_id
        # format as required and return string
        # creating an HTMLWeaver could return html or YAML




class MyParser(DataParser):
    def parse(self, data_file_path):
        output = {}
        for chunk in Path(data_file_path).read_text().split('---'):
            tag, body = chunk.strip().split('\n', maxsplit=1)
            if tag in output:
                raise Exception("Duplicate tag in data file")
            output[tag] = body
        return output


class MyWeaver(Weaver):
    def weave(self, text):
        return md.markdown(text)


class YamlWeaver(Weaver):
    def weave(self, chunk):
        return ''        

class TextLoom(Loom):
    def _process(self, doc_file, data_file, tag_parser=r'\$[A-Z_\-]\$', weave_func=lambda x: x, parser=None):
        paratext = parser.parse(data_file)
        doc_text = Path(doc_file).read_text()
        tags = re.findall(tag_parser, doc_text)
        for tag in tags:
            if tag not in paratext:
                print(tag, "not in paratext data. Continuing")
                continue
            replacement = weave_func(paratext[tag])
            doc_text = doc_text.replace(tag, replacement)
        return doc_text

    def merge_as_textfile(self, doc_file, data_file, tag_parser=r'\$[A-Z_\-]+\$', parser=None):
        print(self.head_template)
        print(self._process(doc_file, data_file, tag_parser, parser=parser))
        print(self.foot_template)

    def merge_with_weaver(self, doc_file, data_file, weaver, tag_parser=r'\$[A-Z_\-]+\$', parser=None):
        print(self.head_template)
        print(self._process(doc_file, data_file, tag_parser, weaver.weave, parser))
        print(self.foot_template)


HEADER = """
<style>

@font-face {
  font-family: 'Cardo';
  src: url('fonts/Cardo-Regular.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Cardo';
  src: url('fonts/Cardo-Bold.ttf') format('truetype');
  font-weight: bold;
  font-style: normal;
}

@font-face {
  font-family: 'Cardo';
  src: url('fonts/Cardo-Italic.ttf') format('truetype');
  font-weight: normal;
  font-style: italic;
}

body {
    font-family: 'Cardo';
    font-size: 1.25em;
}
.container {
  justify-content:center;
  align-items: center;
  display: flex; /* Use flexbox for horizontal alignment */
  flex-direction: row;
  flex-wrap: wrap; /* Allow elements to wrap to the next line */
}

.item {
  text-align:center;
  display: flex;
  align-items: center;
  flex-direction: column;
  width: fit-content; /* 30%;  Adjust width as needed */
  margin: 10px; /* Add spacing between items */
  padding: 10px;
  box-sizing: border-box; /* Include padding in width calculation */
}

.item > p {
    min-width: fit-content;
    block-size: fit-content;
}

@media screen and (max-width: 600px) {
  /* For screens smaller than 600px */
  .container {
    flex-direction: column; /* Stack items vertically */
  }
}

img {width: 100%;}
</style>
"""

if __name__ == '__main__':
    text_file = sys.argv[1]
    paratext_file = sys.argv[2]
    parser = MyParser()
    weaver = MyWeaver()
    loom = TextLoom(head_template=HEADER)
    loom.merge_with_weaver(text_file, paratext_file, weaver, parser=parser)

    

        
