#!/bin/bash
chmod +x run_test.sh
$PWD/python3-virtualenv/bin/python -m unittest discover -v tests/
