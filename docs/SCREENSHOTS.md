# Screenshotting the page

The page's sections start at `opacity: 0` and are revealed by IntersectionObserver or
scroll-driven CSS animations. A screenshot taken before those fire captures an empty band, and
an in-app browser pane can also stop compositing when its window is not frontmost. So a plain
screenshot of this page often comes back blank or half-drawn even when the layout is fine, and
measuring element boxes in JavaScript is not a substitute for looking at it.

## What a trustworthy capture does

Before a single pixel is captured:

1. Drive the system Chrome headless (for example via `playwright-core`), so nothing depends on
   an app window being visible and there is no browser download.
2. Emulate `prefers-reduced-motion`.
3. Inject a stylesheet on init that forces every animation and transition to its finished state
   and un-hides the reveal patterns, so no section can be invisible.
4. Scroll the whole document to trip any IntersectionObserver that survived step 3, then return
   to the top.
5. Wait for fonts, for every image to decode, and for layout to stop changing.

A capture that cannot be trusted (blank frame, an image that never decoded, layout still moving)
must fail loudly with a non-zero exit, never quietly return a dark rectangle.

## The tool

The owner's machines carry a script that does all of the above: `shotpage.mjs`, in the `shot`
folder of the owner's shared Claude tools (it is not vendored into this repo).

```
node shotpage.mjs index.html -o out.png                  full page
node shotpage.mjs index.html --sel "#pricing" -o out.png one section
node shotpage.mjs index.html --each-section outdir/      every <section>, one file each
node shotpage.mjs index.html --width 1400 --mobile       viewport control
```

Without that repo, any headless-browser script that follows the five steps above gives the same
result.
