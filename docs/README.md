# Concept
Functions in a module should be laid out like a newspaper

Most important (the headline) at the top, then subsequent lower layers each with finer detail as we go down.

Functions with no level of indentation should be considered top level

Functions that are not called within the module can be considered the user end points for the module because if they are not called within the module then the intention is to call them from elsewhere.

So we order top level functions by the number of times they are called from lowest to highest count.

Of those, functions that call the most number of other functions in the same module should be near the top as they are pulling together the most amount of module specific processing.

lastly if the function is called the same as another and calls the same number of other functions then we order by name alphabetically.

## Sort methods

### newspaper
`newspaper`: functions that have the least calls themselves and call the most functions, if functions equally ranked with these metrics they are sorted alphabetically. 

The idea is to read functions that are both not called within the module (thus are expected to be called elsewhere) and call the most functions from within the module, giving you the "headline" of the modules functionality while having to read the least but allow you to read internal functions with more detail if necessary in order of importance for the module.

### called
`called`: functions that are called the most are at the top moving to those that are called the least. The idea is to get an idea of the core functionality of a module before reading the code where they are used.

### calls
`calls`: functions that call the most other functions are at the top allowing for efficient reading of the code that "do" the most first.

### alphabetical
`alphabetical`: self-explanatory, excludes leading underscores

example: ["a", "_b", "c"]

### alphabetical_include_leading_underscores
`alphabetical_include_leading_underscores`: self-explanatory, includes leading underscores

example: ["_b", "a", "c"]

## Leading underscores
If a function is:
- internal to another (nested) it is given a leading underscore.
- called by another in the same module it is given a leading underscore.

Otherwise it has no leading underscore.


# To use
```bash
python3 -m headline <cwd> [src_dir] [tests_dir] [sort_type] [tests_only] [rename] [suffix]
```

## args
- `cwd`: the directory to run the process on

- `src_dir`: the directory with the source files, `headline` will match files in this directory to those with the `test_` prefix in the specified tests directory

- `test_dir`: the directory where the test files are for the source files

- `sort_type`: 
    - `newspaper`: sort functions based on a custom "newspaper" logic.                                                 
    - `called`: sort functions by the number of times they are referenced or "called" by other functions               
    - `calls` : sort functions based on the number of references or "calls" they make to other functions               
    - `alphabetical`: sort functions alphabetically, ignoring leading underscores                      
    - `alphabetical_include_leading_underscores`: sort functions alphabetically, including leading underscores in the sort order

- `rename`: add leading underscores to functions that are used internally within the module

- `suffix`: if you want to try `headline` on your code but not apply the changes inplace, this will create files with the suffix you specify, so `my_file.py` with suffix `_example` will have headline applied to it and save to `my_file_example.py`
