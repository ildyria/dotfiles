ping6 services-1.meeting.ietf.org | while read pong; do echo "$(date +%Y-%m-%d_%H:%M:%S): $pong"; done
