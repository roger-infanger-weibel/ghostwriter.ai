"""Schreibt docs/podcast/feed.xml (RSS 2.0 + iTunes-Tags) aus show.yaml und episodes.json."""
from __future__ import annotations

from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


def _dur(sec: int) -> str:
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def build_feed(cfg: dict, episodes: list[dict], site: Path) -> Path:
    base = cfg["base_url"].rstrip("/")
    e = escape
    items = []
    for ep in sorted(episodes, key=lambda x: x["id"], reverse=True):
        url = f"{base}/{ep['file']}"
        post_url = f"{cfg['website']}/blob/main/{ep['post']}"
        desc = f"{ep['description']}\n\nShownotes und Quellen: {post_url}"
        items.append(f"""    <item>
      <title>{e(ep['title'])}</title>
      <description>{e(desc)}</description>
      <link>{e(post_url)}</link>
      <guid isPermaLink="false">ghostwriter-ai-{e(ep['id'])}</guid>
      <pubDate>{e(ep['pub_date'])}</pubDate>
      <enclosure url="{e(url)}" length="{ep['bytes']}" type="audio/mpeg"/>
      <itunes:duration>{_dur(ep['duration_seconds'])}</itunes:duration>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:explicit>{'true' if cfg.get('explicit') else 'false'}</itunes:explicit>
    </item>""")

    # E-Mail nur, wenn in show.yaml gesetzt (nötig erst für Verzeichnisse wie Spotify/Apple)
    owner = ""
    if cfg.get("owner_email"):
        owner = (f"    <itunes:owner>\n      <itunes:name>{e(cfg['author'])}</itunes:name>\n"
                 f"      <itunes:email>{e(cfg['owner_email'])}</itunes:email>\n    </itunes:owner>\n")
    now = format_datetime(datetime.now(timezone.utc).replace(microsecond=0))
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:atom="http://www.w3.org/2005/Atom"
     xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{e(cfg['title'])}</title>
    <link>{e(cfg['website'])}</link>
    <atom:link href="{e(base)}/feed.xml" rel="self" type="application/rss+xml"/>
    <description>{e(cfg['description'])}</description>
    <language>{e(cfg['language'])}</language>
    <lastBuildDate>{now}</lastBuildDate>
    <itunes:subtitle>{e(cfg.get('subtitle', ''))}</itunes:subtitle>
    <itunes:summary>{e(cfg['description'])}</itunes:summary>
    <itunes:author>{e(cfg['author'])}</itunes:author>
{owner}    <itunes:image href="{e(base)}/{e(cfg['cover_file'])}"/>
    <image>
      <url>{e(base)}/{e(cfg['cover_file'])}</url>
      <title>{e(cfg['title'])}</title>
      <link>{e(cfg['website'])}</link>
    </image>
    <itunes:category text="{e(cfg['category'])}"/>
    <itunes:explicit>{'true' if cfg.get('explicit') else 'false'}</itunes:explicit>
    <itunes:type>episodic</itunes:type>
{chr(10).join(items)}
  </channel>
</rss>
"""
    site.mkdir(parents=True, exist_ok=True)
    out = site / "feed.xml"
    out.write_text(xml, encoding="utf-8")
    return out
