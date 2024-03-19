## Dependencies

You will need the `jinja2` and `yaml` packages for Python. You can install them like this:
```
python3 -m pip install jinja2 pyyaml
```

## Usage and directory structure

Here are the purposes of a few directories within this project:

- `data` should contain one or more XML files with resume data
- `conf` should contain one or more YAML files with config data
- `tpl` should contain one or more Jinja templates, of any file extension
- `out` is the directory that will contain the generated resume files

You may generate a resume template as follows:

```
./generate lomax default basic.html
```

This will use the resume data from `data/lomax.xml` and the config file from `conf/default.yml` to substitute information into the `tpl/basic.html` template, and dump the output to `out/lomax_basic.html`.

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
