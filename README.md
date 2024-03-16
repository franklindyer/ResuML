## YAML config format

The following describes each component of the YAML config file that is to be passed to the script.

- `priorities`: assign a numerical value to different element types and tags that you wish to prioritize
- `limits`: assign an upper limit to the number of entries included in a resumé section, sorted by priority

Here's an example of a config file that you might use:

```
priorities:
    webdev: 20
    design: 10
    language: 10
limits:
    skills: 5
```

Using this configuration, the `prioritize` function will assign each of your skills a quantitative priority value. Skills with a `type` or `tag` of `webdev` will receive 20 points, those with `design` will receive `10` points and those with `language` will receive `10` points. The skills will be sorted by this holistic priority value and then truncated after the top 5 skills.
