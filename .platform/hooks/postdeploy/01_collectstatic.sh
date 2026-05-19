#!/bin/bash
source /var/app/venv/*/bin/activate
cd /var/app/current
python manage.py collectstatic --noinput --no-default-ignore
echo "Collectstatic completed successfully"
