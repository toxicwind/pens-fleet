#!/usr/bin/env python3
"""Regenerate index.html from live GitHub metadata (owned, non-fork repos)."""
import subprocess, json, html

def main():
    out = subprocess.run(['gh','api','--paginate','user/repos?per_page=100&affiliation=owner',
                          '--jq','.[] | {name, description, language, html_url, pushed_at, stargazers_count, fork, archived}'],
                         capture_output=True, text=True, check=True, timeout=300).stdout.strip()
    dec, objs, i = json.JSONDecoder(), [], 0
    while i < len(out):
        if out[i] in ' \n': i += 1; continue
        o, i = dec.raw_decode(out, i); objs.append(o)
    objs.sort(key=lambda r: r['pushed_at'] or '', reverse=True)
    data = json.dumps([{"n":r['name'],"d":html.escape(r['description'] or ''),"l":r['language'] or "\u2014",
        "u":(r['pushed_at'] or '')[:10],"s":r['stargazers_count'],"a":r['archived'],"url":r['html_url']}
        for r in objs if not r['fork']], separators=(',',':'))
    tpl = open('index.template.html').read()
    open('index.html','w').write(tpl.replace('__DATA__', data))
    print("index.html regenerated:", len(data), "bytes data")

if __name__ == '__main__':
    main()
