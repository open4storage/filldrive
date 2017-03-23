# filldrive
The filldrive script allows you to create text files in your system based on specific requirements

# Instructions

## Install the requirements


Install Python 3.5 or later then run:

```pip install -r requirements.txt```

# Execute the script

```python ./src/filldrive.py```

This will create a small file by default.  You can use the help command:

```python ./src/filldrive.py -h```

This is the output:
```
usage: filldrive.py [-h] [--filename FILENAME] [--size SIZE] [--unit UNIT]
                    [--count COUNT] [--interval INTERVAL] [--silent]
                    [--no-silent]

The filldrive script allows you to create text files in your system based on
specific requirements

optional arguments:
  -h, --help            show this help message and exit
  --filename FILENAME, -f FILENAME
                        (default: filldrive.fll)
  --size SIZE, -s SIZE  (default: 1)
  --unit UNIT, -u UNIT  (default: B)
  --count COUNT, -c COUNT
                        (default: 1)
  --interval INTERVAL, -i INTERVAL
                        (default: 1)
  --silent
  --no-silent           (default: True)
  ```
