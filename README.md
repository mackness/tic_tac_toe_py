# Summary

A very simple tic tac toe game I wrote mainly to familiarize myself with Python :)

## Usage

Run the following docker comamnd from within the root of the repo
```
docker run -it --rm --name tic-tac-toe -v $(pwd)/tic_tac_toe.py:/src/tic_tac_toe.py: python:3 python /src/tic_tac_toe.py
```