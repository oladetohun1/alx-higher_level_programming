#!/bin/bash
curl -si "$1" | grep -i content-length
