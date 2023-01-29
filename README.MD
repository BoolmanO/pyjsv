
# pyjsv

This library is the easiest way to manipulate data through multiple formats, xml, toml, yaml, json. They are all serialized to dict

(At the moment we only have json and xml format)
## Running Tests

To run tests, run the following command

```bash
  python .\pyjsv\test_all.py
```
## About this project
- simple, with good documentation
- ideal for writing scripts using it
## Usage/Examples

SimpleJson

```python
from pyjsv import SimpleJson

my_parsed_dict =  \
{
    "languages": [
        {"python": ["easy to learn", "slow"]},
        {"cpp": ["hard to learn", "fast"]},
        {"rust": ["easier than cpp but harder than python", "BLAZINGLY FAST :lightning: :lightning: :lightning:"]}
        ]
}

sj = SimpleJson.upload_from_dict(my_parsed_dict)
sj.save_file("my_json.json")
"""Support for yaml, toml will be added in the future.
Data between them will be transferred just as easily."""

```

SimpleXml
```python
from pyjsv import SimpleXml

my_parsed_xml = '''
<data>
    <language name="Python">
        <rank>1</rank>
        <speed>slow</speed>
        <developer country="Netherlands">Guido van Rossum</developer>
    </language>
    <language name="Rust">
        <rank>1</rank>
        <speed>blazingly fast!!11!</speed>
        <developer country="Not Found :(">Graydon Hoare</developer>
    </language>
</data>
'''
sj = SimpleXml.upload_from_str(my_parsed_xml)
sj.save_file("my_xml.xml")

```




## Docs


_IJsonLikeObj
(pyjsv.classes.interfaces.py)

An abstract class that implements a base interface:

- statics:
    - upload_from_str(str) -> Self
    - upload_from_dict(dict) -> Self
    - upload_from_file(os.PathLike) -> Self

- methods:
    - save_file(os.PathLike) -> None // saves the file of its extension to the given path
    - get_dict() -> dict

SimpleJson(_IJsonLikeObj)
(pyjsv.classes.jsv_json.py)
- implement _IJsonLikeObj with no changes


SimpleXml
- statics:
    - upload_from_str(str, text_kw: str, attrs_pref: str) -> Self
    - upload_from_dict(dict, text_kw: str, attrs_pref: str) -> Self
    - upload_from_file(os.PathLike, , text_kw: str, attrs_pref: str) -> Self

- methods:
    - get_xml() -> str // return xml
    - save_file(os.PathLike) -> None // saves the file of its extension to the given path
    - get_dict() -> dict
