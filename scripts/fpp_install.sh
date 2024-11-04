#!/bin/bash
set -x


echo Restarting FPP...
curl http://localhost/api/system/fppd/restart
echo ...Done
