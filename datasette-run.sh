#!/bin/bash

# Get env vars
import .env

# Open Data set
datasette serve $GOODREADS_DB