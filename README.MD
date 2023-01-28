
# pyjsv

This library is the easiest way to manipulate data through multiple formats, xml, toml, yaml, json. They are all serialized to dict

(At the moment we only have json format)
## Running Tests

To run tests, run the following command

```bash
  python .\pyjsv\test_all.py
```
## About this project
- simple, with good documentation
- ideal for writing scripts using it
## Usage/Examples

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

sj = SimpleJson.load_from_dict(my_parsed_dict)
sj.save_file("my_json.json")
"""Support for xml, yaml, toml will be added in the future.
Data between them will be transferred just as easily."""
```

