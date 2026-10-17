"""Wrap the approved header in a self-contained SVG name reveal.

The PNG artwork is embedded unchanged. Only its name-and-marker band is
revealed; the remaining illustration is static. No image processing needed.
"""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "sketchbook"


def string_grid():
    vertical = [f'<path d="M{x} 55 V350"/>' for x in range(1550, 1710, 13)]
    horizontal = [f'<path d="M1540 {y} H1720"/>' for y in range(65, 345, 14)]
    return "".join(vertical + horizontal)


def build(theme):
    png = ASSETS / "header-approved.png"
    encoded = base64.b64encode(png.read_bytes()).decode("ascii")
    # Coordinates use the artwork's original 1774 x 887 viewBox.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1840" height="887" viewBox="0 0 1840 887" role="img" aria-labelledby="title desc">
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
    <mask id="racket-behind-laptop" maskUnits="userSpaceOnUse" x="0" y="0" width="1774" height="887" style="mask-type:luminance">
      <rect width="1774" height="887" fill="white"/>
      <path d="M1100 245 L1620 270 L1590 590 L1048 550 Z" fill="black"/>
    </mask>
    <clipPath id="strings">
      <ellipse cx="1628" cy="201" rx="77" ry="136"/>
    </clipPath>
  </defs>
  <!-- Notebook margin and corrections are separate vector strokes. The approved raster is unchanged. -->
  <path d="M28 18 C25 207 31 362 27 521 S29 744 27 869" fill="none" stroke="#8a6a67" stroke-width="1.5" opacity=".75"/>
  <g transform="translate(54 0)">
  <use xlink:href="#art" mask="url(#outside-name)"/>
  <g class="name"><use xlink:href="#art" clip-path="url(#name-reveal)"/></g>
  <g fill="none" stroke="#3f5871" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M111 644 C27 605 26 533 104 477"/>
    <path d="M85 479 L104 477 L99 495"/>
  </g>
  <g mask="url(#racket-behind-laptop)">
  <g transform="rotate(31 1628 201)" fill="none" stroke="#70879b" stroke-linecap="round">
    <g clip-path="url(#strings)" opacity=".75" stroke-width=".9">
      {string_grid()}
    </g>
    <ellipse cx="1628" cy="201" rx="77" ry="136" stroke-width="1" opacity=".6"/>
  </g>
  </g>
  </g>
</svg>'''
    (ASSETS / f"header-animated-{theme}.svg").write_text(svg + "\n")


if __name__ == "__main__":
    for theme in ("dark", "light"):
        build(theme)
