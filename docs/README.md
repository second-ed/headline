# Concept
Functions in a module should be laid out like a newspaper

Most important (the headline) at the top, then subsequent lower layers each with finer detail as we go down.

Functions with no level of indentation should be considered top level

Functions that are not called within the module can be considered the user end points for the module because if they are not called within the module then the intention is to call them from elsewhere.

So we order top level functions by the number of times they are called from lowest to highest count.

Of those, functions that call the most number of other functions in the same module should be near the top as they are pulling together the most amount of module specific processing.

lastly if the function is called the same as another and calls the same number of other functions then we order by name alphabetically.

## Leading underscores
If a function is:
- internal to another (nested) it is given a leading underscore.
- called by another in the same module it is given a leading underscore.

Otherwise it has no leading underscore.



