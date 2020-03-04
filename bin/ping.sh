ping 8.8.8.8 | while read pong; do echo "$(date +%Y-%m-%d_%H:%M:%S): $pong"; done
