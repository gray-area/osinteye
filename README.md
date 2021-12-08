![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/osinteye?style=flat&logo=github)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/osinteye/badge)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/rlyonheart/osinteye?style=flat&logo=github)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/osinteye?style=flat&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/osinteye?style=flat&logo=github)

A 👥user 🔎reconnaisance tool that extracts a ⭕target's information from Instagram, DockerHub &amp; Github. Also 🔎searches for matching usernames on Github.
![osinteye](https://user-images.githubusercontent.com/74001397/143137199-d3545457-7b78-48d5-9d9d-e6d2623b4a47.gif)


# Features
* extracts Instagram info
* extracts DockerHub info
* extracts Github info (including followers list and repositories)
* searches related usernames on Github


# Installation
![installation](https://user-images.githubusercontent.com/74001397/143138986-c0cf6065-942b-4276-b917-c0bfb17b2a9d.gif)

Clone project:

```
git clone https://github.com/rlyonheart/osinteye.git
```

```
cd osinteye
```

```
pip install -r requirements.txt
```

# Usage
```
python osinteye --[SITENAME] [USERNAME]
```

**Or give osintEye execution permission**:
```
chmod +x osinteye
```

```
./osinteye --[SITENAME] [USERNAME]
```

**Example .1**;
```
python osinteye -v --instagram johndoe
```

**Example .2**;
```
./osinteye -v --instagram johndoe
```

> **Note**: *If no sitename is specified, osintEye will search for the username on all available sites by default*

# Available Sources
* Instagram
* DockerHub
* Github

# Optional Arguments
| Flag        | Usage |
| ------------- |:---------:|
| <code>-I/--instagram</code> |  *[OPTIONAL] get target's Instagram information*  |
| <code>-G/--github</code> |  *[OPTIONAL] get target's Github information*  |
| <code>-D/--dockerhub</code> |  *[OPTIONAL] get target's DockerHub information*  |
| <code>-sG/--github-search</code> | *[OPTIONAL] search username on Github* |
| <code>-r/--raw</code> | *[OPTIONAL] return output in raw json format*  |
| <code>-sU/--shorten-urls</code> |  *[OPTIONAL] if passed, all urls in results will be shortened*  |
| <code>-v/--verbose</code>  | *[RECOMMENDED] run osintEye in verbose mode (returns network logs, errors and warnings)*  |


# Disclaimer
*This tool should not be used in environments withouth legal authorization.
The author [Richard Mwewa](https://about.me/rlyonheart) will not be responsible for the damages that might be done with it.**

# LICENSE
![license](https://user-images.githubusercontent.com/74001397/137917929-2f2cdb0c-4d1d-4e4b-9f0d-e01589e027b5.png)

# About me
* [About.me](https://about.me/rlyonheart)

# Contact me
* [Github](https://github.com/rlyonheart)

* [Twitter](https://twitter.com/rly0nheart)
