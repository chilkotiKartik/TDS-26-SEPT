#!/usr/bin/env bash
set -euo pipefail
mkdir -p replaced
cd replaced
unzip -o ../q-replace-across-files.zip
sed -i 's/iitm/IIT Madras/gI' *
cat * | sha256sum
