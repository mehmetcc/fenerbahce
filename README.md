# Fenerbahce

fenerbahce is a command line tool to fetch information past and future games of Fenerbahçe's Professional Football Team

Currently, only the last and the next game information can be shown. In the future I will integrate live scores, and pip packaging.

## Dependencies

fenerbahce depends on the following packages:

- BeautifulSoup4
- lxml
- click
- requests

## Running

The project is built by using poetry and Python3. So in order to be able to run this project, make sure you have a running Python3 instance and a working poetry distribution.

To run fenerbahce locally, use the command:
```
poetry run fenerbahce
```