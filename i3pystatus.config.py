import logging
from i3pystatus import Status

status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock", format="%a %-d %b %X KW%V",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
status.register("battery",
    format="{status}/{consumption:.2f}W {remaining:%E%hh:%Mm} {percentage:.2f}%]",
    alert=True,
    alert_percentage=10,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)

# Displays whether a DHCP client is running
#status.register("runwatch",
#    name="DHCP",
#    path="/var/run/dhclient*.pid",)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlan0",
    format_up="{essid} {quality:03.0f}%",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
#status.register("disk",
    #path="/",
    #format="{used}/{total}G [{avail}G]",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪{volume}",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)

status.register(
    'backlight',
    format='☀{percentage}%')

status.run()
