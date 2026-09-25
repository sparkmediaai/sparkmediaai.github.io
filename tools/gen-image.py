#!/usr/bin/env python3
"""Generate an image with the OpenAI Images API and save it into the site.

Usage:
  OPENAI_API_KEY=... python3 tools/gen-image.py "prompt text" -o assets/images/social/hero.png
  python3 tools/gen-image.py "prompt" -o out.png --size 1024x1536 --quality high --model gpt-image-2.5-sunburst

The key is read from the OPENAI_API_KEY environment variable only. Never commit it.
Standard library only; honours HTTPS_PROXY and SSL_CERT_FILE like any urllib call.
"""
import argparse
import base64
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

API = "https://api.openai.com/v1/images/generations"

# Keeps generated images on-brand unless --raw is passed.
STYLE = (
    "Photorealistic, natural light, shot on a phone, authentic user-generated-content feel. "
    "True-to-life people with natural skin texture, real proportions and correctly formed hands; "
    "not airbrushed or stylized. No text, no logos, no watermarks. Subtle cool navy and cyan tones."
)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompt")
    ap.add_argument("-o", "--out", required=True, help="output path, e.g. assets/images/social/reel.png")
    ap.add_argument("--model", default=os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2.5-sunburst"))
    ap.add_argument("--size", default="1024x1024", help="1024x1024, 1536x1024 (landscape), 1024x1536 (portrait), or auto")
    ap.add_argument("--quality", default="medium", help="low, medium, high, or auto")
    ap.add_argument("--format", default=None, help="png, jpeg or webp (defaults from the output extension)")
    ap.add_argument("--raw", action="store_true", help="send the prompt as-is, without the house style")
    args = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("OPENAI_API_KEY is not set.")

    fmt = args.format or {".jpg": "jpeg", ".jpeg": "jpeg", ".webp": "webp"}.get(os.path.splitext(args.out)[1].lower(), "png")
    body = {
        "model": args.model,
        "prompt": args.prompt if args.raw else f"{args.prompt}. {STYLE}",
        "size": args.size,
        "quality": args.quality,
        "output_format": fmt,
        "n": 1,
    }
    req = urllib.request.Request(
        API,
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=300) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"OpenAI API error {e.code}: {e.read().decode(errors='replace')}")

    item = data["data"][0]
    if "b64_json" not in item:
        sys.exit(f"Unexpected response: {json.dumps(item)[:400]}")
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "wb") as f:
        f.write(base64.b64decode(item["b64_json"]))
    print(args.out)
    if item.get("revised_prompt"):
        print("revised prompt:", item["revised_prompt"])


if __name__ == "__main__":
    main()
