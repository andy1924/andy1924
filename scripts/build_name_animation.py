"""Wrap the approved header in a self-contained SVG name reveal.

The PNG artwork is embedded unchanged. Only its name-and-marker band is
revealed; the remaining illustration is static. No image processing needed.
"""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "sketchbook"


def build(theme):
    png = ASSETS / f"header-edited-{theme}.png"
    encoded = base64.b64encode(png.read_bytes()).decode("ascii")
    # Coordinates use the artwork's original 1774 x 887 viewBox.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1774" height="887" viewBox="0 0 1774 887" role="img" aria-labelledby="title desc">
  <title id="title">Arnav Deshpande's sketchbook</title>
  <desc id="desc">The handwritten name Arnav appears across a sage marker stroke. The remaining notebook illustration stays still. A curved arrow links NMIMS, Mumbai to Computer Engineering student.</desc>
  <defs>
    <image id="art" width="1774" height="887" xlink:href="data:image/png;base64,{encoded}"/>
    <mask id="outside-name" maskUnits="userSpaceOnUse" x="0" y="0" width="1774" height="887" style="mask-type:luminance">
      <rect width="1774" height="887" fill="white"/>
      <rect x="50" y="208" width="850" height="200" fill="black"/>
    </mask>
    <clipPath id="name-reveal" clipPathUnits="userSpaceOnUse">
      <rect class="ink" x="50" y="208" width="850" height="200"/>
    </clipPath>
    <style>
      .ink {{ animation: write-name 7s linear infinite; }}
      .name {{ animation: reset-name 7s linear infinite; }}
      @keyframes write-name {{
        0% {{ width: 0px; }}
        24%, 100% {{ width: 850px; }}
      }}
      @keyframes reset-name {{
        0%, 90% {{ opacity: 1; }}
        98%, 100% {{ opacity: 0; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .ink, .name {{ animation: none; opacity: 1; }}
      }}
    </style>
  </defs>
  <use xlink:href="#art" mask="url(#outside-name)"/>
  <g class="name"><use xlink:href="#art" clip-path="url(#name-reveal)"/></g>
</svg>'''
    (ASSETS / f"header-animated-{theme}.svg").write_text(svg + "\n")


if __name__ == "__main__":
    for theme in ("dark", "light"):
        build(theme)
