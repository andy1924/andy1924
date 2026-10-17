# Profile design notes

Research and design: 17 October 2026.

## References inspected

- [GitHub: using your profile to enhance your resume](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume): give visitors a clear introduction, curate a small selection of projects, and make those projects easy to explore.
- [DenverCoder1](https://github.com/DenverCoder1/DenverCoder1): distinct sections for original projects, contributions, and tools. Takeaway: make the work easy to find.
- [Sindre Sorhus](https://github.com/sindresorhus/sindresorhus): a playful visual identity with direct links to work. Takeaway: personal interests can define the presentation.
- [Abhishek Naidu](https://github.com/abhisheknaiidu/abhisheknaiidu): personal copy and activity information. Takeaway: a profile can feel like a person lives there.
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme): a reference collection spanning minimal, retro, animated, and interactive approaches. Used to explore the range of formats.

These are qualitative design observations, not evidence that a particular design improves hiring outcomes.

## The original direction: The Curiosity Mix

An animated record sleeve connects Arnav's music interests with the existing Indian print illustrations. Ink blue, vermilion, saffron, and cream carry through the banner and new CARRICK sleeve. The project list becomes four illustrated tracks; engineering caveats become expandable liner notes; personal interests become Side B.

The banner and CARRICK illustration are original, editable SVG assets. The banner uses self-contained CSS animation, has a complete static appearance, and respects reduced-motion preferences. Essential information also appears as selectable README text. The other three project illustrations already existed in the repository.

No profile text or artwork was copied from the reference profiles. No third-party statistics service, access token, or scheduled workflow is needed.

## Suggested profile pins

Order: CARRICK, UdyogSaarthi, Graph-RAG, The-First-Six-Overs, AtlasAI. This puts practical engineering first, followed by research and a memorable personal project. Pins are a separate GitHub setting and have not been changed by this README edit.

## Verification scope

The artwork and README were inspected locally in a browser using a GitHub-style preview. Image paths, image descriptions, SVG syntax, and whitespace were checked. The preview approximates GitHub styling; the updated README has not been published or verified on the live profile.
