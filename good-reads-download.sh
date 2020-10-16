#!/bin/bash

# Get env vars
import .env

# Download book DB
goodreads-to-sqlite books $GOODREADS_DB