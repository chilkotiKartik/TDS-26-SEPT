#!/usr/bin/env bash
set -euo pipefail

unzip -o q-move-rename-files.zip -d extracted
mkdir -p flat
find extracted -type f -exec mv {} flat/ \;

cd flat
for f in *; do
  new=$(echo "$f" | sed 'y/0123456789/1234567890/')
  if [ "$f" != "$new" ]; then mv -- "$f" "$new"; fi
done

grep . * | LC_ALL=C sort | sha256sum
