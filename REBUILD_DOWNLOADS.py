from pathlib import Path
import re, base64, json, mimetypes, io, zipfile
root=Path(__file__).resolve().parent
manifest=(root/"manifest.js").read_text(encoding="utf-8")
galleries={}
for key in ("vc","registrar","meritorious"):
    m=re.search(rf'{key}\s*:\s*\[(.*?)\]',manifest,re.S)
    galleries[key]=re.findall(r'["\']([^"\']+)["\']',m.group(1)) if m else []
downloads={}; zips={}
for g,names in galleries.items():
    downloads[g]={}; valid=[]; seen=set()
    for name in names:
        if name in seen: continue
        seen.add(name); p=root/"images"/g/name
        if p.exists():
            b=p.read_bytes(); mime=mimetypes.guess_type(name)[0] or "application/octet-stream"
            downloads[g][name]=f"data:{mime};base64,"+base64.b64encode(b).decode()
            valid.append((name,b))
    buf=io.BytesIO()
    with zipfile.ZipFile(buf,"w",zipfile.ZIP_DEFLATED) as z:
        for name,b in valid:z.writestr(name,b)
    zips[g]="data:application/zip;base64,"+base64.b64encode(buf.getvalue()).decode()
(root/"downloads-data.js").write_text(
    "window.EMBEDDED_DOWNLOADS="+json.dumps(downloads,separators=(",",":"))+";\n"+
    "window.GALLERY_ZIPS="+json.dumps(zips,separators=(",",":"))+";\n",encoding="utf-8")
print("downloads-data.js rebuilt successfully.")
