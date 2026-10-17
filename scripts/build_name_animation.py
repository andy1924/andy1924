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


def annotation_regions(fill="white"):
    # These tight polygons follow the three existing slanted notes.
    # They keep the original handwriting; only the ink color changes.
    polygons = (
        "912,292 1063,248 1074,300 923,340",
        "775,542 868,516 881,549 784,580",
        "1650,805 1774,761 1774,801 1720,824 1650,839",
    )
    return "".join(f'<polygon points="{p}" fill="{fill}"/>' for p in polygons)


def punch_holes():
    return "".join(
        f'''<g transform="translate(24 {y})">
          <ellipse rx="13" ry="14" fill="#27303b" opacity=".45"/>
          <ellipse rx="10.5" ry="11.5" fill="url(#punch-shade)" stroke="#5f6670" stroke-width=".8" stroke-opacity=".55"/>
          <path d="M-8 6 Q0 12 8 6" fill="none" stroke="#8a9198" stroke-width=".8" opacity=".35"/>
          <path d="M-8 -5 Q-1 -12 7 -6" fill="none" stroke="#02050a" stroke-width="1.7" opacity=".8"/>
        </g>'''
        for y in (150, 443, 736)
    )


def build(theme):
    png = ASSETS / "header-approved.png"
    encoded = base64.b64encode(png.read_bytes()).decode("ascii")
    # Coordinates use the artwork's original 1774 x 887 viewBox.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1870" height="887" viewBox="0 0 1870 887" role="img" aria-labelledby="title desc">
  <title id="title">Arnav Deshpande's sketchbook</title>
  <desc id="desc">The handwritten name Arnav appears across a sage marker stroke. The remaining notebook illustration stays still. A curved arrow links NMIMS, Mumbai to Computer Engineering student.</desc>
  <defs>
    <image id="art" width="1774" height="887" xlink:href="data:image/png;base64,{encoded}"/>
    <mask id="outside-name" maskUnits="userSpaceOnUse" x="0" y="0" width="1774" height="887" style="mask-type:luminance">
      <rect width="1774" height="887" fill="white"/>
      <rect x="50" y="208" width="850" height="200" fill="black"/>
      {annotation_regions("black")}
    </mask>
    <clipPath id="annotation-letters" clipPathUnits="userSpaceOnUse">{annotation_regions()}</clipPath>
    <filter id="faint-orange" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feColorMatrix type="matrix" values="0 0 0 0 .76  0 0 0 0 .51  0 0 0 0 .36  0 0 0 .72 0"/>
    </filter>
    <radialGradient id="punch-shade" cx="35%" cy="27%" r="85%">
      <stop offset="0" stop-color="#02050a"/>
      <stop offset=".65" stop-color="#0a1018"/>
      <stop offset="1" stop-color="#303a46"/>
    </radialGradient>
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
  {punch_holes()}
  <path d="M56 18 C53 207 59 362 55 521 S57 744 55 869" fill="none" stroke="#8a6a67" stroke-width="1.5" opacity=".75"/>
  <g transform="translate(84 0)">
  <use xlink:href="#art" mask="url(#outside-name)"/>
  <g class="name"><use xlink:href="#art" clip-path="url(#name-reveal)"/></g>
  <use xlink:href="#art" clip-path="url(#annotation-letters)" filter="url(#faint-orange)"/>
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
