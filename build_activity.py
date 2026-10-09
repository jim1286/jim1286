from collections import OrderedDict
from datetime import datetime
from pathlib import Path
import json
import subprocess

root = Path(__file__).parent
query = '{ user(login:"jim1286") { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } } } }'
data = json.loads(subprocess.check_output(["gh", "api", "graphql", "-f", f"query={query}"], text=True))
calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
days = [day for week in calendar["weeks"] for day in week["contributionDays"]]
monthly = OrderedDict()
for day in days:
    month = day["date"][:7]
    monthly[month] = monthly.get(month, 0) + day["contributionCount"]
total = calendar["totalContributions"]
assert total == sum(day["contributionCount"] for day in days)
active = sum(day["contributionCount"] > 0 for day in days)
recent = sum(day["contributionCount"] for day in days[-30:])
last = days[-1]["date"]
max_month = max(monthly.values()) or 1

# GitHub owns the native contribution/activity UI. A dated, repository-owned
# SVG offers a custom summary without CSS injection or fake live statistics.
for theme in ["light", "dark"]:
    p = ({"bg": "#f6f7fb", "ink": "#182235", "muted": "#64748b", "line": "#e1e6ef", "accent": "#5366dc", "bar": "#b9c3f5"}
         if theme == "light" else
         {"bg": "#151b27", "ink": "#edf1f8", "muted": "#a2aec3", "line": "#303b50", "accent": "#a2afff", "bar": "#596da2"})
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="340" viewBox="0 0 960 340" role="img" aria-labelledby="title desc">
<title id="title">Development activity</title><desc id="desc">{total:,} contributions, {active} active days, {recent:,} contributions in the last 30 days. Snapshot {last}.</desc>
<rect width="960" height="340" rx="20" fill="{p['bg']}"/>
<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif">
<text x="36" y="36" font-size="11" font-weight="600" letter-spacing="1.8" fill="{p['muted']}">DEVELOPMENT ACTIVITY</text>
<text x="924" y="36" text-anchor="end" font-size="11" fill="{p['muted']}">SNAPSHOT · {last}</text>''']
    for x, value, label in [(36, f"{total:,}", "CONTRIBUTIONS / YEAR"), (355, str(active), "DAYS WITH CONTRIBUTIONS"), (674, f"{recent:,}", "CONTRIBUTIONS / 30 DAYS")]:
        parts.append(f'<text x="{x}" y="97" font-size="43" font-weight="650" letter-spacing="-1" fill="{p["ink"]}">{value}</text><text x="{x}" y="121" font-size="10" letter-spacing="1.1" fill="{p["muted"]}">{label}</text>')
    parts.append(f'<path d="M36 151H924M36 283H924" stroke="{p["line"]}" fill="none"/>')
    step = 888 / len(monthly)
    for i, (month, count) in enumerate(monthly.items()):
        x = 36 + step * i + 10
        h = 105 * count / max_month
        color = p["accent"] if i == len(monthly) - 1 else p["bar"]
        parts.append(f'<rect x="{x:.1f}" y="{283-h:.1f}" width="{step-20:.1f}" height="{max(h,2):.1f}" rx="5" fill="{color}"><title>{month}: {count} contributions</title></rect>')
        parts.append(f'<text x="{x+(step-20)/2:.1f}" y="{max(283-h-7,166):.1f}" text-anchor="middle" font-size="10" fill="{p["muted"]}">{count}</text>')
        label = datetime.strptime(month, "%Y-%m").strftime("%b")
        parts.append(f'<text x="{x+(step-20)/2:.1f}" y="303" text-anchor="middle" font-size="11" fill="{p["muted"]}">{label}</text>')
    parts.append(f'<text x="36" y="327" font-size="10" fill="{p["muted"]}">{days[0]["date"]} — {last} · monthly totals; boundary months are partial</text></g></svg>')
    (root / "assets" / f"activity-{theme}.svg").write_text("\n".join(parts))
print(f"Activity snapshot: {total:,} contributions / {active} active days / {recent:,} in 30 days / {last}")
